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
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.Gravity;
import android.view.KeyEvent;
import android.view.View;
import android.view.View.OnSystemUiVisibilityChangeListener;
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

import com.google.android.play.core.assetpacks.*;
import com.google.android.play.core.assetpacks.model.*;
import com.google.android.play.core.tasks.OnSuccessListener;

public class PythonSDLActivity extends SDLActivity implements AssetPackStateUpdateListener {

    /**
     * This exists so python code can access this activity.
     */
    public static PythonSDLActivity mActivity = null;

    /**
     * The layout that contains the SDL view. VideoPlayer uses this to add
     * its own view on on top of the SDL view.
     */
    public FrameLayout mFrameLayout;

    /**
     * A layout that contains mLayout. This is a 3x3 grid, with the layout
     * in the center. The idea is that if someone wants to show an ad, they
     * can stick it in one of the other cells..
     */
    public LinearLayout mVbox;

    /**
     * This is set by the renpy.iap.Store when it's loaded. If it's not loadable, this
     * remains null;
     */
    public StoreInterface mStore = null;

    ResourceManager resourceManager;

    protected String[] getLibraries() {
        return new String[] {
            "renpython",
        };
    }

    // Creates the IAP store, when needed. /////////////////////////////////////////

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

    // GUI code. /////////////////////////////////////////////////////////////

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


    // Overriding this makes SDL respect the orientation given in the Android
    // manifest.
    @Override
    public void setOrientationBis(int w, int h, boolean resizable, String hint) {
        return;
    }

    // Code to unpack python and get things running ///////////////////////////

    public void recursiveDelete(File f) {
        if (f.isDirectory()) {
            for (File r : f.listFiles()) {
                recursiveDelete(r);
            }
        }
        f.delete();
    }

    /**
     * This determines if unpacking one the zip files included in
     * the .apk is necessary. If it is, the zip file is unpacked.
     */
    public void unpackData(final String resource, File target) {

        /**
         * Delete main.pyo unconditionally. This fixes a problem where we have
         * a main.py newer than main.pyo, but start.c won't run it.
         */
        new File(target, "main.pyo").delete();

        boolean shouldUnpack = false;

        // The version of data in memory and on disk.
        String data_version = resourceManager.getString(resource + "_version");
        String disk_version = null;

        String filesDir = target.getAbsolutePath();
        String disk_version_fn = filesDir + "/" + resource + ".version";

        // If no version, no unpacking is necessary.
        if (data_version != null) {

            try {
                byte buf[] = new byte[64];
                InputStream is = new FileInputStream(disk_version_fn);
                int len = is.read(buf);
                disk_version = new String(buf, 0, len);
                is.close();
            } catch (Exception e) {
                disk_version = "";
            }

            if (! data_version.equals(disk_version)) {
                shouldUnpack = true;
            }
        }


        // If the disk data is out of date, extract it and write the
        // version file.
        if (shouldUnpack) {
            Log.v("python", "Extracting " + resource + " assets.");

            // Delete old libraries & renpy files.
            recursiveDelete(new File(target, "lib"));
            recursiveDelete(new File(target, "renpy"));

            target.mkdirs();

            AssetExtract ae = new AssetExtract(this);
            if (!ae.extractTar(resource + ".mp3", target.getAbsolutePath())) {
                toastError("Could not extract " + resource + " data.");
            }

            try {
                // Write .nomedia.
                new File(target, ".nomedia").createNewFile();

                // Write version file.
                FileOutputStream os = new FileOutputStream(disk_version_fn);
                os.write(data_version.getBytes());
                os.close();
            } catch (Exception e) {
                Log.w("python", e);
            }
        }

    }

    /**
     * Show an error using a toast. (Only makes sense from non-UI
     * threads.)
     */
    public void toastError(final String msg) {

        final Activity thisActivity = this;

        runOnUiThread(new Runnable () {
            public void run() {
                Toast.makeText(thisActivity, msg, Toast.LENGTH_LONG).show();
            }
        });

        // Wait to show the error.
        synchronized (this) {
            try {
                this.wait(1000);
            } catch (InterruptedException e) {
            }
        }
    }

    public native void nativeSetEnv(String variable, String value);

    public void preparePython() {
        Log.v("python", "Starting preparePython.");

        mActivity = this;

        resourceManager = new ResourceManager(this);

        File oldExternalStorage = new File(Environment.getExternalStorageDirectory(), getPackageName());
        File externalStorage = getExternalFilesDir(null);
        File path;

        if (externalStorage == null) {
            externalStorage = oldExternalStorage;
        }

        unpackData("private", getFilesDir());

        nativeSetEnv("ANDROID_PRIVATE", getFilesDir().getAbsolutePath());
        nativeSetEnv("ANDROID_PUBLIC",  externalStorage.getAbsolutePath());
        nativeSetEnv("ANDROID_OLD_PUBLIC", oldExternalStorage.getAbsolutePath());

        // Figure out the APK path.
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

    };

    // App lifecycle.
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

    boolean mAllPacksReady = false;
    AssetPackManager mAssetPackManager = null;

    // The pack download progress bar.
    ProgressBar mProgressBar = null;

    /**
     * Given a pack name, return true if it's been downloaded and is
     * ready for use, or false otherwise. Returns true if the pack
     * doesn't exist at all.
     */
    boolean checkPack(String name) {
        AssetPackLocation location = mAssetPackManager.getPackLocation(name);
        if (location != null) {
            nativeSetEnv("ANDROID_PACK_" + name.toUpperCase(), location.assetsPath());
            return true;
        } else {
            return false;
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.v("python", "onCreate()");
        super.onCreate(savedInstanceState);

        // Initalize the store support.
        createStore();

        boolean allPacksReady = true;

        if (Constants.assetPacks.length > 0) {

            mAssetPackManager = AssetPackManagerFactory.getInstance(this);
            mAssetPackManager.registerListener(this);

            for (String pack : Constants.assetPacks) {
                if (! checkPack(pack) ) {
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

        // Show the presplash.
        Bitmap presplashBitmap = getBitmap(bitmapFilename + ".png");

        if (presplashBitmap == null) {
            presplashBitmap = getBitmap(bitmapFilename + ".jpg");
        }

        if (presplashBitmap != null) {

            mPresplash = new ImageView(this);
            mPresplash.setBackgroundColor(presplashBitmap.getPixel(0, 0));
            mPresplash.setScaleType(ImageView.ScaleType.FIT_CENTER);
            mPresplash.setImageBitmap(presplashBitmap);

            mLayout.addView(mPresplash, new ViewGroup.LayoutParams(ViewGroup.LayoutParams.FILL_PARENT, ViewGroup.LayoutParams.FILL_PARENT));
        }

        if (!mAllPacksReady) {
            RelativeLayout.LayoutParams prlp = new RelativeLayout.LayoutParams(ViewGroup.LayoutParams.FILL_PARENT, 20);
            prlp.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);
            prlp.leftMargin = 20;
            prlp.rightMargin = 20;
            prlp.bottomMargin = 20;

            mProgressBar = new ProgressBar(this, null, android.R.attr.progressBarStyleHorizontal);
            mLayout.addView(mProgressBar, prlp);
        }

    }

    /**
     * Called by Ren'Py to hide the presplash after start.
     */
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
    }

    @Override
    protected void onNewIntent(Intent intent) {
        Log.v("python", "onNewIntent()");
        setIntent(intent);
    }


    boolean waitForWifiConfirmationShown = false;
    HashMap<String, AssetPackState> assetPackStates = new HashMap<String, AssetPackState>();

    long mOldProgress = 0;

    public void onStateUpdate(AssetPackState assetPackState) {
        Log.i("packs", "onStateUpdate: " + assetPackState.toString());

        assetPackStates.put(assetPackState.name(), assetPackState);

        switch (assetPackState.status()) {
          case AssetPackStatus.PENDING:
            break;

          case AssetPackStatus.DOWNLOADING:
            break;

          case AssetPackStatus.TRANSFERRING:
            break;

          case AssetPackStatus.COMPLETED:
            break;

          case AssetPackStatus.FAILED:
            Log.e("python", "error = " + assetPackState.errorCode());
            break;

          case AssetPackStatus.CANCELED:
            break;

          case AssetPackStatus.WAITING_FOR_WIFI:
            if (!waitForWifiConfirmationShown) {
              mAssetPackManager.showCellularDataConfirmation(mActivity)
                .addOnSuccessListener(new OnSuccessListener<Integer> () {
                  @Override
                  public void onSuccess(Integer resultCode) {
                    if (resultCode == RESULT_OK) {
                      Log.d("python", "Confirmation dialog has been accepted.");
                    } else if (resultCode == RESULT_CANCELED) {
                      Log.d("python", "Confirmation dialog has been denied by the user.");
                    }
                  }
                });
              waitForWifiConfirmationShown = true;
            }
            break;

          case AssetPackStatus.NOT_INSTALLED:
            break;
        }

        // Check all the asset packs again.
        boolean allPacksReady = true;

        long totalBytesToDownload = 0;
        long bytesDownloaded = 0;

        if (Constants.assetPacks.length > 0) {
            for (String pack : Constants.assetPacks) {
                if (! checkPack(pack) ) {
                    allPacksReady = false;
                }

                AssetPackState aps = assetPackStates.get(pack);
                if (aps != null) {
                    totalBytesToDownload += aps.totalBytesToDownload();
                    bytesDownloaded += aps.bytesDownloaded();
                }
            }
        }

        Log.d("packs", "totalBytesToDownload=" + totalBytesToDownload + ", bytesDownloaded=" + bytesDownloaded);

        // Protect against a DBZ.
        if (totalBytesToDownload == 0) {
            totalBytesToDownload = 1;
        }

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


    // Support public APIs. ////////////////////////////////////////////////////

    public void openUrl(String url) {
        openURL(url);
    }

    public void vibrate(double s) {
        Vibrator v = (Vibrator) getSystemService(Context.VIBRATOR_SERVICE);
        if (v != null) {
            v.vibrate((int) (1000 * s));
        }
    }

    public int getDPI() {
        DisplayMetrics metrics = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(metrics);
        return metrics.densityDpi;
    }

    public PowerManager.WakeLock wakeLock = null;

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

    // Activity Requests ///////////////////////////////////////////////////////

    // The thought behind this is that this will make it possible to call
    // mActivity.startActivity(Intent, requestCode), then poll the fields on
    // this object until the response comes back.

    public int mActivityResultRequestCode = -1;
    public int mActivityResultResultCode = -1;
    public Intent mActivityResultResultData = null;

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent resultData) {
        if (mStore != null && mStore.onActivityResult(requestCode, resultCode, resultData)) {
            return;
        }

        Log.v("python", "onActivityResult(" + requestCode + ", " + resultCode + ", " + resultData.toString() + ")");

        mActivityResultRequestCode = requestCode;
        mActivityResultResultCode = resultCode;
        mActivityResultResultData = resultData;

        super.onActivityResult(requestCode, resultCode, resultData);
    }
}
