package org.renpy.android;

import org.libsdl.app.SDLActivity;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.ClipData;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageManager;
import android.content.pm.PackageManager.NameNotFoundException;
import android.database.Cursor;
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

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

import com.google.android.play.core.assetpacks.*;
import com.google.android.play.core.assetpacks.model.*;
import com.google.android.gms.tasks.*;

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

    // ---------- SAF / Mod import flags ----------
    private boolean mModImportFinished = false;   // Tells preparePython that import is done (or skipped)

    // UI elements for custom boot loading dialog
    private ProgressBar mLoadingProgressBar = null;
    private android.widget.TextView mLoadingStatusText = null;

    // Request codes for SAF intents
    private static final int SAF_FOLDER_REQUEST_CODE = 998;
    private static final int SAF_PICKER_REQUEST_CODE  = 999;

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

        // Wait for asset packs AND for mod import to finish (if user chose to import)
        if (!mAllPacksReady || !mModImportFinished) {
            Log.i("python", "Waiting for all packs and mod import to become ready.");
        }

        synchronized (this) {
            while (!mAllPacksReady || !mModImportFinished) {
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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.v("python", "onCreate()");
        super.onCreate(savedInstanceState);

        if (mLayout == null) {
            return;
        }

        // Show the mod import dialog before anything else
        showImportModDialog();
    }

    /**
     * Continues the normal Ren'Py boot process (original onCreate code after dialog).
     */
    private void continueRenpyBoot() {
        // Initialize the store support.
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

                // Backstop.
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

    public void armOnStop () {
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
          case AssetPackStatus.PENDING:
            break;

          case AssetPackStatus.DOWNLOADING:
            break;

          case AssetPackStatus.TRANSFERRING:
            break;

          case AssetPackStatus.COMPLETED:
            break;

          case AssetPackStatus.FAILED:
            Toast.makeText(this, "Download of " + assetPackState.name() + " failed. Error " + assetPackState.errorCode(), Toast.LENGTH_LONG).show();
            Log.e("python", "error = " + assetPackState.errorCode());

          case AssetPackStatus.CANCELED:
            mAssetPackManager.fetch(Collections.singletonList(assetPackState.name()));
            break;

          case AssetPackStatus.WAITING_FOR_WIFI:
          case AssetPackStatus.REQUIRES_USER_CONFIRMATION:
            mAssetPackManager.showConfirmationDialog(this);
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

        Log.v("python", "onActivityResult(" + requestCode + ", " + resultCode + ", " + (resultData != null ? resultData.toString() : "null") + ")");

        mActivityResultRequestCode = requestCode;
        mActivityResultResultCode = resultCode;
        mActivityResultResultData = resultData;

        // Handle SAF file picker result
        if (requestCode == SAF_PICKER_REQUEST_CODE) {
            if (resultCode == Activity.RESULT_OK && resultData != null) {
                handleSAFSelection(resultData);
            } else {
                if (!mModImportFinished) {
                    // User cancelled import, continue normal boot
                    continueRenpyBoot();
                    synchronized (this) {
                        mModImportFinished = true;
                        this.notifyAll();
                    }
                }
            }
            return;
        }

        // Handle SAF folder picker result
        if (requestCode == SAF_FOLDER_REQUEST_CODE) {
            if (resultCode == Activity.RESULT_OK && resultData != null) {
                handleFolderSelection(resultData);
            } else {
                if (!mModImportFinished) {
                    continueRenpyBoot();
                    synchronized (this) {
                        mModImportFinished = true;
                        this.notifyAll();
                    }
                }
            }
            return;
        }

        super.onActivityResult(requestCode, resultCode, resultData);
    }

    // ======================== SAF (Storage Access Framework) Methods ========================

    /**
     * Shows the initial dialog asking the user whether they want to import mods before starting the game.
     */
    private void showImportModDialog() {
        new android.app.AlertDialog.Builder(this)
            .setTitle("Import Mods")
            .setMessage("Do you want to import a mod folder before starting the game?")
            .setPositiveButton("Yes, Import", (dialog, which) -> openSAFPicker())
            .setNegativeButton("No, Start Game", (dialog, which) -> {
                continueRenpyBoot();
                synchronized (PythonSDLActivity.this) {
                    mModImportFinished = true;
                    PythonSDLActivity.this.notifyAll();
                }
            })
            .setCancelable(false)
            .show();
    }

    /**
     * Opens a dialog to choose between importing single files or a whole folder.
     */
    public void openSAFPicker() {
        runOnUiThread(() -> {
            new android.app.AlertDialog.Builder(PythonSDLActivity.this)
                .setTitle("Import Mods")
                .setMessage("What do you want to import?")
                .setPositiveButton("Files", (dialog, which) -> openSAFPickerForRPA())
                .setNegativeButton("Entire folder", (dialog, which) -> openSAFPickerForFolder())
                .setNeutralButton("Cancel", null)
                .show();
        });
    }

    /**
     * Opens the system file picker for multiple files (RPA, RPY, RPYC).
     */
    public void openSAFPickerForRPA() {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("*/*");
        intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
        startActivityForResult(intent, SAF_PICKER_REQUEST_CODE);
    }

    /**
     * Opens the system folder picker (document tree).
     */
    public void openSAFPickerForFolder() {
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT_TREE);
        startActivityForResult(intent, SAF_FOLDER_REQUEST_CODE);
    }

    /**
     * Handles the result of the file picker: copies each selected file to the game directory.
     */
    private void handleSAFSelection(final Intent resultData) {
        final File externalFilesDir = getExternalFilesDir(null);
        if (externalFilesDir == null) {
            toastError("External storage not available.");
            if (!mModImportFinished) {
                continueRenpyBoot();
                synchronized (PythonSDLActivity.this) {
                    mModImportFinished = true;
                    PythonSDLActivity.this.notifyAll();
                }
            }
            return;
        }

        final File gameDir = new File(externalFilesDir, "game");
        if (!gameDir.exists()) gameDir.mkdirs();

        // Show appropriate loading dialog (custom during boot, simple progress otherwise)
        final android.app.Dialog loadingUI;
        if (!mModImportFinished) {
            loadingUI = createBootLoadingDialog("COPYING FILES...");
            loadingUI.show();
        } else {
            ProgressDialog pd = new ProgressDialog(this);
            pd.setTitle("Copying files...");
            pd.setMessage("Please wait.");
            pd.setIndeterminate(true);
            pd.setCancelable(false);
            pd.show();
            loadingUI = pd;
        }

        new Thread(() -> {
            final boolean isBootFlow = !mModImportFinished;
            ClipData clipData = resultData.getClipData();
            final int totalUris = (clipData != null) ? clipData.getItemCount() : 1;
            int filesCopied = 0;
            final List<Uri> copiedUris = new ArrayList<>();

            // Collect all URIs
            Uri[] uris = new Uri[totalUris];
            if (clipData != null) {
                for (int i = 0; i < totalUris; i++) uris[i] = clipData.getItemAt(i).getUri();
            } else {
                uris[0] = resultData.getData();
            }

            // Copy each file with progress tracking
            for (Uri uri : uris) {
                if (uri == null) continue;

                String name = null;
                long fileSize = -1;
                Cursor cursor = getContentResolver().query(uri,
                    new String[]{ DocumentsContract.Document.COLUMN_DISPLAY_NAME, DocumentsContract.Document.COLUMN_SIZE },
                    null, null, null);
                if (cursor != null) {
                    try {
                        if (cursor.moveToFirst()) {
                            name = cursor.getString(0);
                            if (!cursor.isNull(1)) fileSize = cursor.getLong(1);
                        }
                    } finally { cursor.close(); }
                }
                if (name == null) continue;

                String lower = name.toLowerCase();
                if (!lower.endsWith(".rpa") && !lower.endsWith(".rpy") && !lower.endsWith(".rpyc")) {
                    Log.w("python", "Unsupported file: " + name);
                    continue;
                }

                // Update status on boot loading screen
                if (isBootFlow) {
                    runOnUiThread(() -> {
                        if (mLoadingStatusText != null) mLoadingStatusText.setText(name);
                        if (mLoadingProgressBar != null) mLoadingProgressBar.setProgress(0);
                    });
                }

                // Copy file with byte-by-byte progress
                try (InputStream in = getContentResolver().openInputStream(uri);
                     FileOutputStream out = new FileOutputStream(new File(gameDir, name))) {
                    if (in == null) continue;
                    byte[] buf = new byte[65536];
                    int b;
                    long bytesCopied = 0;
                    while ((b = in.read(buf)) != -1) {
                        out.write(buf, 0, b);
                        if (isBootFlow && fileSize > 0) {
                            bytesCopied += b;
                            final int pct = (int) (100L * bytesCopied / fileSize);
                            runOnUiThread(() -> {
                                if (mLoadingProgressBar != null) mLoadingProgressBar.setProgress(pct);
                            });
                        }
                    }
                    out.flush();
                    filesCopied++;
                    copiedUris.add(uri);
                    Log.i("python", "Copied: " + name);
                } catch (Exception e) {
                    Log.e("python", "Error copying " + name + ": " + e);
                }
            }

            final int count = filesCopied;
            final List<Uri> finalCopiedUris = copiedUris;
            runOnUiThread(() -> {
                // Clean up loading UI
                mLoadingProgressBar = null;
                mLoadingStatusText = null;
                loadingUI.dismiss();

                if (!mModImportFinished) {
                    // Boot flow: ask whether to delete original files
                    new android.app.AlertDialog.Builder(PythonSDLActivity.this)
                        .setTitle("Delete original files?")
                        .setMessage("All files have been copied to the game folder.\n\nDo you want to delete the original files from their source location?")
                        .setPositiveButton("Yes, delete", (dialog, which) -> {
                            for (Uri u : finalCopiedUris) {
                                try {
                                    DocumentsContract.deleteDocument(getContentResolver(), u);
                                    Log.i("python", "Deleted original: " + u.toString());
                                } catch (Exception e) {
                                    Log.e("python", "Failed to delete original: " + e);
                                }
                            }
                            continueRenpyBoot();
                            synchronized (PythonSDLActivity.this) {
                                mModImportFinished = true;
                                PythonSDLActivity.this.notifyAll();
                            }
                        })
                        .setNegativeButton("No, keep them", (dialog, which) -> {
                            continueRenpyBoot();
                            synchronized (PythonSDLActivity.this) {
                                mModImportFinished = true;
                                PythonSDLActivity.this.notifyAll();
                            }
                        })
                        .setCancelable(false)
                        .show();
                } else {
                    // In-game flow (if called from elsewhere)
                    new android.app.AlertDialog.Builder(PythonSDLActivity.this)
                        .setTitle("Files copied!")
                        .setMessage(count + " file(s) copied.\n\nThe originals will be deleted from their source location.")
                        .setCancelable(false)
                        .setPositiveButton("Delete & continue", (d, w) -> {
                            for (Uri u : finalCopiedUris) {
                                try {
                                    DocumentsContract.deleteDocument(getContentResolver(), u);
                                } catch (Exception e) { Log.e("python", "Failed to delete original: " + e); }
                            }
                            d.dismiss();
                        })
                        .setNegativeButton("Delete & close", (d, w) -> {
                            for (Uri u : finalCopiedUris) {
                                try {
                                    DocumentsContract.deleteDocument(getContentResolver(), u);
                                } catch (Exception e) { Log.e("python", "Failed to delete original: " + e); }
                            }
                            android.os.Process.killProcess(android.os.Process.myPid());
                        })
                        .show();
                }
            });
        }).start();
    }

    /**
     * Handles the result of the folder picker: recursively copies all supported files.
     */
    private void handleFolderSelection(final Intent resultData) {
        final File externalFilesDir = getExternalFilesDir(null);
        if (externalFilesDir == null) {
            toastError("External storage not available.");
            return;
        }

        final File gameDir = new File(externalFilesDir, "game");
        if (!gameDir.exists()) gameDir.mkdirs();

        final Uri treeUri = resultData.getData();
        if (treeUri == null) return;

        final android.app.Dialog loadingUI;
        if (!mModImportFinished) {
            loadingUI = createBootLoadingDialog("COPYING FOLDER...");
            loadingUI.show();
        } else {
            ProgressDialog pd = new ProgressDialog(this);
            pd.setTitle("Copying folder...");
            pd.setMessage("Please wait.");
            pd.setIndeterminate(true);
            pd.setCancelable(false);
            pd.show();
            loadingUI = pd;
        }

        new Thread(() -> {
            final int[] count = {0};
            String rootDocId = DocumentsContract.getTreeDocumentId(treeUri);
            Uri rootUri = DocumentsContract.buildDocumentUriUsingTree(treeUri, rootDocId);
            copyDocumentNodeRecursive(treeUri, rootUri, gameDir, count);

            runOnUiThread(() -> {
                mLoadingProgressBar = null;
                mLoadingStatusText = null;
                loadingUI.dismiss();

                new android.app.AlertDialog.Builder(PythonSDLActivity.this)
                    .setTitle("Folder copied successfully!")
                    .setMessage(count[0] + " file(s) copied.\n\nTo load new files you need to restart the game.\n\nDo you want to close it now?")
                    .setCancelable(false)
                    .setPositiveButton("Close game", (dialog, which) -> android.os.Process.killProcess(android.os.Process.myPid()))
                    .setNegativeButton("Continue playing", (dialog, which) -> {
                        dialog.dismiss();
                        if (!mModImportFinished) {
                            continueRenpyBoot();
                            synchronized (PythonSDLActivity.this) {
                                mModImportFinished = true;
                                PythonSDLActivity.this.notifyAll();
                            }
                        }
                    })
                    .show();
            });
        }).start();
    }

    /**
     * Recursively copies a document tree using the Storage Access Framework.
     *
     * @param treeUri the root tree URI
     * @param docUri  the current document URI
     * @param destDir destination directory on app's private storage
     * @param count   array to hold the number of copied files
     */
    private void copyDocumentNodeRecursive(Uri treeUri, Uri docUri, File destDir, int[] count) {
        String mimeType = null;
        String displayName = null;
        long fileSize = -1;

        try (Cursor cursor = getContentResolver().query(docUri,
                new String[]{ DocumentsContract.Document.COLUMN_MIME_TYPE,
                              DocumentsContract.Document.COLUMN_DISPLAY_NAME,
                              DocumentsContract.Document.COLUMN_SIZE },
                null, null, null)) {
            if (cursor != null && cursor.moveToFirst()) {
                mimeType = cursor.getString(0);
                displayName = cursor.getString(1);
                if (!cursor.isNull(2)) fileSize = cursor.getLong(2);
            }
        }

        // Handle directory: recurse into children
        if (DocumentsContract.Document.MIME_TYPE_DIR.equals(mimeType)) {
            File subDir = (displayName != null) ? new File(destDir, displayName) : destDir;
            String docId = DocumentsContract.getDocumentId(docUri);
            Uri childrenUri = DocumentsContract.buildChildDocumentsUriUsingTree(treeUri, docId);
            try (Cursor childCursor = getContentResolver().query(childrenUri,
                    new String[]{ DocumentsContract.Document.COLUMN_DOCUMENT_ID },
                    null, null, null)) {
                if (childCursor != null) {
                    while (childCursor.moveToNext()) {
                        String childDocId = childCursor.getString(0);
                        Uri childUri = DocumentsContract.buildDocumentUriUsingTree(treeUri, childDocId);
                        copyDocumentNodeRecursive(treeUri, childUri, subDir, count);
                    }
                }
            }
            return;
        }

        // Handle file: copy only if extension is supported
        if (displayName == null) return;
        String lower = displayName.toLowerCase();
        boolean supported = lower.endsWith(".rpa") || lower.endsWith(".rpy") || lower.endsWith(".rpyc") ||
                            lower.endsWith(".png") || lower.endsWith(".jpg") || lower.endsWith(".jpeg") ||
                            lower.endsWith(".webp") || lower.endsWith(".gif") ||
                            lower.endsWith(".mp4") || lower.endsWith(".mov") || lower.endsWith(".mkv") ||
                            lower.endsWith(".webm") || lower.endsWith(".mp3") || lower.endsWith(".ogg") ||
                            lower.endsWith(".wav");
        if (!supported) {
            Log.w("python", "Folder: ignoring: " + displayName);
            return;
        }

        if (!destDir.exists()) destDir.mkdirs();

        final String fname = displayName;
        runOnUiThread(() -> {
            if (mLoadingStatusText != null) mLoadingStatusText.setText(fname);
            if (mLoadingProgressBar != null) mLoadingProgressBar.setProgress(0);
        });

        try (InputStream in = getContentResolver().openInputStream(docUri);
             FileOutputStream out = new FileOutputStream(new File(destDir, displayName))) {
            if (in == null) return;
            byte[] buf = new byte[65536];
            int b;
            long bytesCopied = 0;
            while ((b = in.read(buf)) != -1) {
                out.write(buf, 0, b);
                if (fileSize > 0) {
                    bytesCopied += b;
                    final int pct = (int) (100L * bytesCopied / fileSize);
                    runOnUiThread(() -> {
                        if (mLoadingProgressBar != null) mLoadingProgressBar.setProgress(pct);
                    });
                }
            }
            out.flush();
            count[0]++;
            Log.i("python", "Folder: copied " + displayName);
        } catch (Exception e) {
            Log.e("python", "Folder: error copying " + displayName + ": " + e);
        }
    }

    /**
     * Creates a fullscreen loading dialog with a spinner, status text, and a horizontal progress bar.
     * Used during the initial boot import process.
     *
     * @param title the title shown above the progress bar
     * @return the created dialog
     */
    private android.app.Dialog createBootLoadingDialog(String title) {
        android.app.Dialog dialog = new android.app.Dialog(this, android.R.style.Theme_Black_NoTitleBar_Fullscreen);
        dialog.setCancelable(false);

        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setGravity(Gravity.CENTER);
        root.setBackgroundColor(android.graphics.Color.parseColor("#1a1a1a"));
        root.setPadding(60, 60, 60, 60);

        // Circular spinner
        ProgressBar spinner = new ProgressBar(this);
        spinner.setIndeterminate(true);
        LinearLayout.LayoutParams spinnerParams = new LinearLayout.LayoutParams(220, 220);
        spinnerParams.gravity = Gravity.CENTER_HORIZONTAL;
        spinnerParams.bottomMargin = 40;
        root.addView(spinner, spinnerParams);

        // Title text
        android.widget.TextView titleTxt = new android.widget.TextView(this);
        titleTxt.setText(title);
        titleTxt.setTextColor(android.graphics.Color.parseColor("#CCCCCC"));
        titleTxt.setTextSize(android.util.TypedValue.COMPLEX_UNIT_SP, 16);
        titleTxt.setGravity(Gravity.CENTER);
        titleTxt.setLetterSpacing(0.2f);
        LinearLayout.LayoutParams titleParams = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        titleParams.gravity = Gravity.CENTER_HORIZONTAL;
        titleParams.bottomMargin = 12;
        root.addView(titleTxt, titleParams);

        // Status text (current file name)
        mLoadingStatusText = new android.widget.TextView(this);
        mLoadingStatusText.setText("");
        mLoadingStatusText.setTextColor(android.graphics.Color.parseColor("#888888"));
        mLoadingStatusText.setTextSize(android.util.TypedValue.COMPLEX_UNIT_SP, 12);
        mLoadingStatusText.setGravity(Gravity.CENTER);
        LinearLayout.LayoutParams statusParams = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        statusParams.gravity = Gravity.CENTER_HORIZONTAL;
        statusParams.bottomMargin = 32;
        root.addView(mLoadingStatusText, statusParams);

        // Progress bar (0-100)
        mLoadingProgressBar = new ProgressBar(this, null, android.R.attr.progressBarStyleHorizontal);
        mLoadingProgressBar.setIndeterminate(false);
        mLoadingProgressBar.setMax(100);
        mLoadingProgressBar.setProgress(0);
        LinearLayout.LayoutParams barParams = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, 8);
        barParams.gravity = Gravity.CENTER_HORIZONTAL;
        root.addView(mLoadingProgressBar, barParams);

        dialog.setContentView(root);
        return dialog;
    }
										  }
