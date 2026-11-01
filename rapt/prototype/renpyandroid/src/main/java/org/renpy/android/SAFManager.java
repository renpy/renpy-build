package org.renpy.android;

import android.app.Activity;
import android.content.ClipData;
import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.net.Uri;
import android.os.ParcelFileDescriptor;
import android.os.PowerManager;
import android.os.Process;
import android.os.SystemClock;
import android.provider.DocumentsContract;
import android.util.Log;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
import java.nio.channels.Channels;
import java.nio.channels.FileChannel;
import java.nio.channels.ReadableByteChannel;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.concurrent.Callable;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.RejectedExecutionException;
import java.util.concurrent.Semaphore;
import java.util.concurrent.atomic.AtomicBoolean;

public class SAFManager {

    private static final String TAG = "SAFManager";
    private static final int REQUEST_CODE_PICK_FILES = 999;

    private static final long PROGRESS_THROTTLE_MS = 100;
    private static final long NIO_CHUNK_SIZE = 4 * 1024 * 1024L;
    private static final int FALLBACK_BUFFER_SIZE = 8 * 1024 * 1024;
    private static final int NIO_CONCURRENCY = 2;
    private static final int COPY_POOL_SIZE = 4;

    private static final int STATUS_START = 0;
    private static final int STATUS_DONE = 100;
    private static final int STATUS_ERROR = -1;
    private static final int STATUS_INVALID_EXT = -2;

    private final PythonSDLActivity activity;
    private final AtomicBoolean importing = new AtomicBoolean(false);
    private final Semaphore nioSlots = new Semaphore(NIO_CONCURRENCY);

    private final ExecutorService copyPool = Executors.newFixedThreadPool(COPY_POOL_SIZE, r -> {
        Thread t = new Thread(() -> {
            Process.setThreadPriority(Process.THREAD_PRIORITY_DEFAULT);
            r.run();
        });
        t.setName("SAFManager-copy");
        return t;
    });

    private final ThreadLocal<ByteBuffer> fallbackBuffer =
            ThreadLocal.withInitial(() -> ByteBuffer.allocateDirect(FALLBACK_BUFFER_SIZE));

    private final PowerManager.WakeLock wakeLock;

    public SAFManager(PythonSDLActivity activity) {
        this.activity = activity;
        PowerManager pm = (PowerManager) activity.getSystemService(Context.POWER_SERVICE);
        this.wakeLock = pm.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "SAFManager:import");
    }

    public boolean openFilePicker() {
        if (!importing.compareAndSet(false, true)) {
            activity.toastError("Import already in progress.");
            return false;
        }

        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.setType("*/*");
        intent.putExtra(Intent.EXTRA_ALLOW_MULTIPLE, true);
        activity.startActivityForResult(intent, REQUEST_CODE_PICK_FILES);
        return true;
    }

    public boolean onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode != REQUEST_CODE_PICK_FILES) return false;

        if (resultCode != Activity.RESULT_OK || data == null) {
            importing.set(false);
            activity.onImportCancelled();
            return true;
        }

        startCopyFiles(data);
        return true;
    }

    public void shutdown() {
        copyPool.shutdown();
    }

    private void startCopyFiles(Intent data) {
        File gameDir = activity.getGameDir();
        if (gameDir == null) {
            importing.set(false);
            activity.toastError("External storage not available.");
            activity.onImportCancelled();
            return;
        }

        List<Uri> uris = extractUris(data);
        if (uris.isEmpty()) {
            importing.set(false);
            activity.onImportCancelled();
            return;
        }

        new Thread(() -> runImportBatch(gameDir, uris), "SAFManager-dispatch").start();
    }

    private List<Uri> extractUris(Intent data) {
        List<Uri> uris = new ArrayList<>();
        ClipData clipData = data.getClipData();
        if (clipData != null) {
            for (int i = 0; i < clipData.getItemCount(); i++) {
                uris.add(clipData.getItemAt(i).getUri());
            }
        } else if (data.getData() != null) {
            uris.add(data.getData());
        }
        return uris;
    }

    private List<CopyJob> resolveJobs(List<Uri> uris) {
        List<CopyJob> jobs = new ArrayList<>();
        Set<String> usedNames = new HashSet<>();

        for (Uri uri : uris) {
            FileInfo info = getFileInfo(uri);
            if (info == null) continue;

            if (!isRpaFile(info.name)) {
                activity.updateImportProgress(STATUS_INVALID_EXT, info.name);
                continue;
            }

            jobs.add(new CopyJob(uri, uniqueName(info.name, usedNames), info.size));
        }
        return jobs;
    }

    private void runImportBatch(File gameDir, List<Uri> uris) {
        long batchStart = SystemClock.elapsedRealtime();
        List<Uri> copiedUris = new CopyOnWriteArrayList<>();

        wakeLock.acquire(10 * 60 * 1000L);
        try {
            List<CopyJob> jobs = resolveJobs(uris);

            if (jobs.isEmpty()) {
                importing.set(false);
                return;
            }

            List<Callable<Void>> tasks = new ArrayList<>();
            for (CopyJob job : jobs) {
                tasks.add(() -> {
                    if (copyJob(job, gameDir)) copiedUris.add(job.uri);
                    return null;
                });
            }

            runTasks(tasks);
        } finally {
            if (wakeLock.isHeld()) wakeLock.release();
        }

        finishBatch(batchStart, copiedUris);
    }

    private void runTasks(List<Callable<Void>> tasks) {
        List<Future<Void>> futures;
        try {
            futures = copyPool.invokeAll(tasks);
        } catch (RejectedExecutionException e) {
            Log.e(TAG, "Copy pool unavailable", e);
            return;
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return;
        }

        for (Future<Void> f : futures) {
            try {
                f.get();
            } catch (ExecutionException e) {
                Log.e(TAG, "Erro inesperado na cópia", e.getCause());
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }

    private boolean copyJob(CopyJob job, File gameDir) {
        File destFile = new File(gameDir, job.name);

        if (!hasEnoughSpace(destFile, job.size)) {
            activity.updateImportProgress(STATUS_ERROR, job.name);
            return false;
        }

        activity.updateImportProgress(STATUS_START, job.name);
        return copyUriToFile(job.uri, destFile, job.size);
    }

    private void finishBatch(long batchStart, List<Uri> copiedUris) {
        long elapsed = SystemClock.elapsedRealtime() - batchStart;
        importing.set(false);

        activity.runOnUiThread(() -> {
            activity.setLastImportDuration(elapsed);
            if (!copiedUris.isEmpty()) {
                activity.setPendingDeletion(new ArrayList<>(copiedUris));
                activity.updateImportProgress(STATUS_DONE, "Done");
            } else {
                activity.updateImportProgress(STATUS_ERROR, "No files");
            }
        });
    }

    private boolean copyUriToFile(Uri sourceUri, File destFile, long fileSize) {
        try {
            nioSlots.acquire();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return copyUriToFileStream(sourceUri, destFile, fileSize);
        }

        long start = SystemClock.elapsedRealtime();
        boolean success;
        try (
            ParcelFileDescriptor pfd = activity.getContentResolver().openFileDescriptor(sourceUri, "r");
            FileChannel inChannel = new FileInputStream(pfd.getFileDescriptor()).getChannel()
        ) {
            long size = (fileSize > 0) ? fileSize : inChannel.size();
            try (FileChannel outChannel = openPreallocatedChannel(destFile, size)) {
                long position = 0;
                long lastUpdate = 0;

                while (position < size) {
                    // limita cada transferTo a NIO_CHUNK_SIZE para gerar múltiplas atualizações de progresso
                    long toTransfer = Math.min(size - position, NIO_CHUNK_SIZE);
                    long n = inChannel.transferTo(position, toTransfer, outChannel);
                    if (n <= 0) break;
                    position += n;

                    long now = SystemClock.elapsedRealtime();
                    if (now - lastUpdate >= PROGRESS_THROTTLE_MS) {
                        lastUpdate = now;
                        activity.updateImportProgress((int) (100L * position / size), destFile.getName());
                    }
                }

                if (position < size) {
                    throw new IOException("Transferência incompleta: " + position + "/" + size + " bytes.");
                }

                Log.i(TAG, "Copied (NIO): " + destFile.getName() + " em " + (SystemClock.elapsedRealtime() - start) + "ms");
                success = true;
            }
        } catch (IOException | SecurityException e) {
            Log.w(TAG, "NIO path failed for " + destFile.getName() + ", falling back: " + e.getMessage());
            success = false;
        } finally {
            nioSlots.release();
        }

        return success || copyUriToFileStream(sourceUri, destFile, fileSize);
    }

    private boolean copyUriToFileStream(Uri sourceUri, File destFile, long fileSize) {
        long start = SystemClock.elapsedRealtime();
        try (InputStream in = activity.getContentResolver().openInputStream(sourceUri)) {
            if (in == null) return false;

            try (FileChannel out = openPreallocatedChannel(destFile, fileSize)) {
                ReadableByteChannel src = Channels.newChannel(in);
                ByteBuffer buf = fallbackBuffer.get();
                buf.clear();
                long total = 0;
                long lastUpdate = 0;
                int read;

                while ((read = src.read(buf)) != -1) {
                    buf.flip();
                    while (buf.hasRemaining()) out.write(buf);
                    buf.clear();
                    total += read;

                    long now = SystemClock.elapsedRealtime();
                    if (fileSize > 0 && now - lastUpdate >= PROGRESS_THROTTLE_MS) {
                        lastUpdate = now;
                        activity.updateImportProgress((int) (100L * total / fileSize), destFile.getName());
                    }
                }

                out.truncate(total);
                Log.i(TAG, "Copied (stream): " + destFile.getName() + " em " + (SystemClock.elapsedRealtime() - start) + "ms");
                return true;
            }
        } catch (IOException | SecurityException e) {
            Log.e(TAG, "Copy error: " + destFile.getName(), e);
            destFile.delete();
            activity.updateImportProgress(STATUS_ERROR, destFile.getName());
            return false;
        }
    }

    private FileChannel openPreallocatedChannel(File destFile, long size) throws IOException {
        RandomAccessFile raf = new RandomAccessFile(destFile, "rw");
        try {
            if (size > 0) raf.setLength(size);
            return raf.getChannel();
        } catch (IOException e) {
            raf.close();
            throw e;
        }
    }

    private boolean hasEnoughSpace(File destFile, long size) {
        if (size <= 0) return true;
        File parent = destFile.getParentFile();
        return parent == null || parent.getUsableSpace() >= size;
    }

    private boolean isRpaFile(String filename) {
        return filename.toLowerCase(Locale.ROOT).endsWith(".rpa");
    }

    private String uniqueName(String name, Set<String> usedNames) {
        if (usedNames.add(name)) return name;

        String base = name.substring(0, name.length() - 4);
        String candidate;
        int i = 1;
        do {
            candidate = base + "_" + i + ".rpa";
            i++;
        } while (!usedNames.add(candidate));
        return candidate;
    }

    private FileInfo getFileInfo(Uri uri) {
        String name = null;
        long size = -1;
        try (Cursor cursor = activity.getContentResolver().query(uri,
                new String[]{DocumentsContract.Document.COLUMN_DISPLAY_NAME,
                             DocumentsContract.Document.COLUMN_SIZE},
                null, null, null)) {
            if (cursor != null && cursor.moveToFirst()) {
                name = cursor.getString(0);
                if (!cursor.isNull(1)) size = cursor.getLong(1);
            }
        } catch (Exception e) {
            Log.e(TAG, "Failed to query: " + uri, e);
        }
        return (name != null) ? new FileInfo(name, size) : null;
    }

    private static class FileInfo {
        String name;
        long size;
        FileInfo(String name, long size) { this.name = name; this.size = size; }
    }

    private static class CopyJob {
        final Uri uri;
        final String name;
        final long size;
        CopyJob(Uri uri, String name, long size) { this.uri = uri; this.name = name; this.size = size; }
    }
}