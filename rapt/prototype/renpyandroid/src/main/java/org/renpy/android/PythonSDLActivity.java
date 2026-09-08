package org.renpy.android;

import org.libsdl.app.SDLActivity;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.content.pm.PackageManager.NameNotFoundException;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.os.PowerManager;
import android.os.Vibrator;
import android.os.VibrationEffect;
import android.provider.DocumentsContract;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.Toast;
import android.widget.ProgressBar;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.RejectedExecutionException;

import com.google.android.play.core.assetpacks.*;
import com.google.android.play.core.assetpacks.model.*;
import com.google.android.gms.tasks.*;

public class PythonSDLActivity extends SDLActivity implements AssetPackStateUpdateListener {

    public static PythonSDLActivity mActivity = null;
    public FrameLayout mFrameLayout;
    public LinearLayout mVbox;
    public StoreInterface mStore = null;
    ResourceManager resourceManager;

    private SAFManager safManager;
    private SaveData saveData;

    public boolean mAllPacksReady = false;
    private AssetPackManager mAssetPackManager;

    public volatile int importProgress = 0;
    public volatile String importFileName = "";
    public volatile List<Uri> pendingDeletionUris = null;
    public volatile long lastImportDurationMs = 0;
    public volatile boolean cleanupInProgress = false;

    private final Object importStateLock = new Object();
    private volatile File cachedGameDir = null;

    private final ExecutorService cleanupExecutor = Executors.newSingleThreadExecutor(
            r -> new Thread(r, "SAFManager-cleanup"));

    protected String[] getLibraries() {
        return new String[] {
            "renpython",
        };
    }

    public void createStore() {
        if (Constants.store.equals("none")) {
            return;
        }
        try {
            Class cls = Class.forName("org.renpy.iap.Store");
            cls.getMethod("create", PythonSDLActivity.class).invoke(null, this);
        } catch (Exception e) {
            Log.e("PythonSDLActivity", "Failed to create store: " + e.toString());
        }
    }

    public void addView(View view, int index) {
        mVbox.addView(view, index, new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT, (float) 0.0));
    }

    public void removeView(View view) {
        mVbox.removeView(view);
    }

    @Override
    public void setContentView(View view) {
        mFrameLayout = new FrameLayout(this);
        mFrameLayout.addView(view);

        mVbox = new LinearLayout(this);
        mVbox.setOrientation(LinearLayout.VERTICAL);
        mVbox.addView(mFrameLayout, new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, 0, (float) 1.0));

        super.setContentView(mVbox);
    }

    @Override
    public void setOrientationBis(int w, int h, boolean resizable, String hint) {
        return;
    }

    public void recursiveDelete(File f) {
        if (f.isDirectory()) {
            File[] children = f.listFiles();
            if (children != null) {
                for (File r : children) {
                    recursiveDelete(r);
                }
            }
        }
        f.delete();
    }

    public void unpackData(final String resource, File target) {
        new File(target, "main.pyo").delete();

        boolean shouldUnpack = false;
        String data_version = resourceManager.getString(resource + "_version");
        String disk_version = null;
        String filesDir = target.getAbsolutePath();
        String disk_version_fn = filesDir + "/" + resource + ".version";

        if (data_version != null) {
            try (InputStream is = new FileInputStream(disk_version_fn)) {
                byte buf[] = new byte[64];
                int len = is.read(buf);
                disk_version = new String(buf, 0, len);
            } catch (Exception e) {
                disk_version = "";
            }
            if (!data_version.equals(disk_version)) {
                shouldUnpack = true;
            }
        }

        if (shouldUnpack) {
            Log.v("python", "Extracting " + resource + " assets.");
            recursiveDelete(new File(target, "lib"));
            recursiveDelete(new File(target, "renpy"));
            target.mkdirs();
            AssetExtract ae = new AssetExtract(this);
            if (!ae.extractTar(resource + ".mp3", target.getAbsolutePath())) {
                toastError("Could not extract " + resource + " data.");
            }
            try {
                new File(target, ".nomedia").createNewFile();
                try (FileOutputStream os = new FileOutputStream(disk_version_fn)) {
                    os.write(data_version.getBytes());
                }
            } catch (Exception e) {
                Log.w("python", e);
            }
        }
    }

    public void toastError(final String msg) {
        final Activity thisActivity = this;
        runOnUiThread(new Runnable() {
            public void run() {
                Toast.makeText(thisActivity, msg, Toast.LENGTH_LONG).show();
            }
        });
        synchronized (this) {
            try {
                this.wait(1000);
            } catch (InterruptedException e) {
            }
        }
    }

    public void toastMessage(final String msg) {
        final Activity thisActivity = this;
        runOnUiThread(new Runnable() {
            public void run() {
                Toast.makeText(thisActivity, msg, Toast.LENGTH_LONG).show();
            }
        });
    }

    public native void nativeSetEnv(String variable, String value);

    public void preparePython() {
        Log.v("python", "Starting preparePython.");
        mActivity = this;
        resourceManager = new ResourceManager(this);

        File oldExternalStorage = new File(Environment.getExternalStorageDirectory(), getPackageName());
        File externalStorage = getExternalFilesDir(null);

        if (externalStorage == null) {
            externalStorage = oldExternalStorage;
        }

        unpackData("private", getFilesDir());
        nativeSetEnv("ANDROID_PRIVATE", getFilesDir().getAbsolutePath());
        nativeSetEnv("ANDROID_PUBLIC",  externalStorage.getAbsolutePath());
        nativeSetEnv("ANDROID_OLD_PUBLIC", oldExternalStorage.getAbsolutePath());

        String apkFilePath;
        ApplicationInfo appInfo;
        PackageManager packMgmr = getApplication().getPackageManager();
        try {
            appInfo = packMgmr.getApplicationInfo(getPackageName(), 0);
            apkFilePath = appInfo.sourceDir;
        } catch (NameNotFoundException e) {
            apkFilePath = "";
        }
        nativeSetEnv("ANDROID_APK", apkFilePath);

        if (!mAllPacksReady) {
            Log.i("python", "Waiting for all packs to become ready.");
        }
        synchronized (this) {
            while (!mAllPacksReady) {
                try {
                    this.wait();
                } catch (InterruptedException e) { /* pass */ }
            }
        }
        Log.v("python", "Finished preparePython.");
    }

    public ImageView mPresplash = null;

    Bitmap getBitmap(String assetName) {
        try {
            InputStream is = getAssets().open(assetName);
            Bitmap rv = BitmapFactory.decodeStream(is);
            is.close();
            return rv;
        } catch (IOException e) {
            return null;
        }
    }

    ProgressBar mProgressBar = null;

    boolean checkPack(String name) {
        AssetPackLocation location = mAssetPackManager.getPackLocation(name);
        if (location != null) {
            if (location.assetsPath() != null) {
                nativeSetEnv("ANDROID_PACK_" + name.toUpperCase(), location.assetsPath());
            } else {
                AssetLocation loc = mAssetPackManager.getAssetLocation(name, "00_pack.txt");
                if (loc != null) {
                    nativeSetEnv("ANDROID_PACK_" + name.toUpperCase(), loc.path());
                }
            }
            return true;
        } else {
            return false;
        }
    }

    public void continueRenpyBoot() {
        createStore();
        boolean allPacksReady = true;

        if (Constants.assetPacks.length > 0) {
            mAssetPackManager = AssetPackManagerFactory.getInstance(this);
            mAssetPackManager.registerListener(this);

            for (String pack : Constants.assetPacks) {
                if (!checkPack(pack)) {
                    Log.i("python", "fetching: " + pack);
                    mAssetPackManager.fetch(Collections.singletonList(pack));
                    allPacksReady = false;
                }
            }
        }

        mAllPacksReady = allPacksReady;
        String bitmapFilename;
        if (allPacksReady) {
            bitmapFilename = "android-presplash";
        } else {
            bitmapFilename = "android-downloading";
        }

        Bitmap presplashBitmap = getBitmap(bitmapFilename + ".png");
        if (presplashBitmap == null) {
            presplashBitmap = getBitmap(bitmapFilename + ".jpg");
        }

        if (presplashBitmap != null) {
            mPresplash = new ImageView(this);
            mPresplash.setBackgroundColor(presplashBitmap.getPixel(0, 0));
            mPresplash.setScaleType(ImageView.ScaleType.FIT_CENTER);
            mPresplash.setImageBitmap(presplashBitmap);
            mLayout.addView(mPresplash, new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        }

        if (!mAllPacksReady) {
            RelativeLayout.LayoutParams prlp = new RelativeLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, 20);
            prlp.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);
            prlp.leftMargin = 20;
            prlp.rightMargin = 20;
            prlp.bottomMargin = 20;

            mProgressBar = new ProgressBar(this, null, android.R.attr.progressBarStyleHorizontal);
            mLayout.addView(mProgressBar, prlp);
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.v("python", "onCreate()");
        super.onCreate(savedInstanceState);

        if (mLayout == null) {
            return;
        }

        safManager = new SAFManager(this);
        saveData = new SaveData(this);

        continueRenpyBoot();
    }

    public void hidePresplash() {
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                if (mActivity.mPresplash != null) {
                    mActivity.mLayout.removeView(mActivity.mPresplash);
                    mActivity.mPresplash = null;
                }
                if (mActivity.mProgressBar != null) {
                    mActivity.mLayout.removeView(mActivity.mProgressBar);
                    mActivity.mProgressBar = null;
                }
            }
        });
    }

    @Override
    protected void onDestroy() {
        Log.v("python", "onDestroy()");
        super.onDestroy();
        if (mStore != null) {
            mStore.destroy();
        }
        if (safManager != null) {
            safManager.shutdown();
        }
        cleanupExecutor.shutdown();
    }

    @Override
    protected void onNewIntent(Intent intent) {
        Log.v("python", "onNewIntent()");
        setIntent(intent);
    }

    public boolean mStopDone = true;

    @Override
    public void onStop() {
        Log.v("python", "onStop() start.");
        super.onStop();
        long startTime = System.currentTimeMillis();
        synchronized (this) {
            while (true) {
                if (mStopDone) {
                    break;
                }
                if (startTime + 8000 < System.currentTimeMillis()) {
                    break;
                }
                try {
                    this.wait(100);
                } catch (InterruptedException e) { /* pass */ }
            }
        }
        Log.v("python", "onStop() done.");
    }

    public void armOnStop() {
        Log.v("python", "armOnStop()");
        mStopDone = false;
    }

    public void finishOnStop() {
        Log.v("python", "finishOnStop()");
        synchronized (this) {
            mStopDone = true;
            this.notifyAll();
        }
    }

    HashMap<String, AssetPackState> assetPackStates = new HashMap<String, AssetPackState>();
    long mOldProgress = 0;

    public void onStateUpdate(AssetPackState assetPackState) {
        Log.i("packs", "onStateUpdate: " + assetPackState.toString());
        assetPackStates.put(assetPackState.name(), assetPackState);

        switch (assetPackState.status()) {
            case AssetPackStatus.FAILED:
                Toast.makeText(this, "Download of " + assetPackState.name() + " failed. Error " + assetPackState.errorCode(), Toast.LENGTH_LONG).show();
                Log.e("python", "error = " + assetPackState.errorCode());
                break;
            case AssetPackStatus.CANCELED:
                mAssetPackManager.fetch(Collections.singletonList(assetPackState.name()));
                break;
            case AssetPackStatus.WAITING_FOR_WIFI:
            case AssetPackStatus.REQUIRES_USER_CONFIRMATION:
                mAssetPackManager.showConfirmationDialog(this);
                break;
            default:
                break;
        }

        boolean allPacksReady = true;
        long totalBytesToDownload = 0;
        long bytesDownloaded = 0;

        if (Constants.assetPacks.length > 0) {
            for (String pack : Constants.assetPacks) {
                if (!checkPack(pack)) {
                    allPacksReady = false;
                }
                AssetPackState aps = assetPackStates.get(pack);
                if (aps != null) {
                    totalBytesToDownload += aps.totalBytesToDownload();
                    bytesDownloaded += aps.bytesDownloaded();
                }
            }
        }

        if (totalBytesToDownload == 0) totalBytesToDownload = 1;
        final long newProgress = 100 * bytesDownloaded / totalBytesToDownload;
        if (mOldProgress != newProgress) {
            mOldProgress = newProgress;
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    if (mProgressBar != null) {
                        mProgressBar.setProgress((int) newProgress);
                    }
                }
            });
        }

        synchronized (this) {
            mAllPacksReady = allPacksReady;
            this.notifyAll();
        }
    }

    public void openUrl(String url) {
        openURL(url);
    }

    public void openEditor(String file) {
        File f = new File(file);
        Uri uri = null;
        if (Build.VERSION.SDK_INT >= 24) {
            uri = RenPyFileProvider.getUriForFile(this, getPackageName() + ".fileprovider", f);
        } else {
            uri = Uri.fromFile(f);
        }
        Intent i = new Intent(Intent.ACTION_VIEW);
        i.setDataAndType(uri, "text/plain");
        i.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION | Intent.FLAG_ACTIVITY_NEW_TASK);
        startActivity(i);
    }

    public void vibrate(double s) {
        Vibrator v = (Vibrator) getSystemService(Context.VIBRATOR_SERVICE);
        if (v != null) {
            if (Build.VERSION.SDK_INT >= 26) {
                v.vibrate(VibrationEffect.createOneShot((int) (1000 * s), VibrationEffect.DEFAULT_AMPLITUDE));
            } else {
                v.vibrate((int) (1000 * s));
            }
        }
    }

    public int getDPI() {
        DisplayMetrics metrics = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(metrics);
        return metrics.densityDpi;
    }

    private PowerManager.WakeLock wakeLock = null;

    public void setWakeLock(boolean active) {
        if (wakeLock == null) {
            PowerManager pm = (PowerManager) getSystemService(Context.POWER_SERVICE);
            wakeLock = pm.newWakeLock(PowerManager.SCREEN_BRIGHT_WAKE_LOCK, "Screen On");
            wakeLock.setReferenceCounted(false);
        }
        if (active) {
            wakeLock.acquire();
        } else {
            wakeLock.release();
        }
    }

    public File getGameDir() {
        File dir = cachedGameDir;
        if (dir != null) return dir;

        synchronized (importStateLock) {
            dir = cachedGameDir;
            if (dir != null) return dir;

            File ext = getExternalFilesDir(null);
            if (ext == null) {
                ext = new File(Environment.getExternalStorageDirectory(), getPackageName());
            }
            dir = new File(ext, "game");
            if (!dir.exists()) dir.mkdirs();

            cachedGameDir = dir;
            return dir;
        }
    }

    public int mActivityResultRequestCode = -1;
    public int mActivityResultResultCode = -1;
    public Intent mActivityResultResultData = null;

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent resultData) {
        if (mStore != null && mStore.onActivityResult(requestCode, resultCode, resultData)) {
            return;
        }

        if (saveData != null && saveData.onActivityResult(requestCode, resultCode, resultData)) {
            return;
        }

        if (safManager != null && safManager.onActivityResult(requestCode, resultCode, resultData)) {
            return;
        }

        Log.v("python", "onActivityResult(" + requestCode + ", " + resultCode + ", " + resultData + ")");
        mActivityResultRequestCode = requestCode;
        mActivityResultResultCode = resultCode;
        mActivityResultResultData = resultData;
        super.onActivityResult(requestCode, resultCode, resultData);
    }

    public SAFManager getSafManager() {
        return safManager;
    }

    public SaveData getSaveData() {
        return saveData;
    }

    public void updateImportProgress(int percent, String fileName) {
        synchronized (importStateLock) {
            this.importProgress = percent;
            this.importFileName = (fileName != null) ? fileName : "";
        }
    }

    public int getImportProgress() {
        synchronized (importStateLock) {
            return this.importProgress;
        }
    }

    public String getImportFileName() {
        synchronized (importStateLock) {
            return this.importFileName;
        }
    }

    public void setLastImportDuration(long durationMs) {
        this.lastImportDurationMs = durationMs;
    }

    public void onImportCancelled() {
        Log.i("python", "Import cancelled by user.");
    }

    public void setPendingDeletion(List<Uri> uris) {
        synchronized (importStateLock) {
            if (this.pendingDeletionUris == null) {
                this.pendingDeletionUris = new ArrayList<>();
            }
            this.pendingDeletionUris.addAll(uris);
        }
    }

    public void deletePendingUris() {
        final List<Uri> toDelete;
        synchronized (importStateLock) {
            if (pendingDeletionUris == null) return;
            toDelete = pendingDeletionUris;
            pendingDeletionUris = null;
        }
        if (toDelete.isEmpty()) return;

        cleanupInProgress = true;
        try {
            cleanupExecutor.execute(() -> {
                try {
                    for (Uri uri : toDelete) {
                        try {
                            DocumentsContract.deleteDocument(getContentResolver(), uri);
                            Log.i("python", "Deleted original: " + uri.toString());
                        } catch (Exception e) {
                            Log.e("python", "Failed to delete original: " + uri, e);
                        }
                    }
                } finally {
                    cleanupInProgress = false;
                }
            });
        } catch (RejectedExecutionException e) {
            Log.w("python", "Cleanup executor unavailable, skipped " + toDelete.size() + " deletions.");
            cleanupInProgress = false;
        }
    }
						}
