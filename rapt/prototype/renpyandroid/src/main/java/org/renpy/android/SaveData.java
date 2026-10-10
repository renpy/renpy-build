package org.renpy.android;

import android.app.Activity;
import android.content.Intent;
import android.database.Cursor;
import android.net.Uri;
import android.os.ParcelFileDescriptor;
import android.provider.DocumentsContract;
import android.util.Log;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.util.concurrent.atomic.AtomicBoolean;

public class SaveData {

    private static final String TAG = "SaveData";
    private static final int REQUEST_CODE_EXPORT_SAVES = 998;
    private static final int REQUEST_CODE_IMPORT_SAVES = 997;

    private final PythonSDLActivity activity;
    private final AtomicBoolean busy = new AtomicBoolean(false);

    public SaveData(PythonSDLActivity activity) {
        this.activity = activity;
    }

    public boolean openSaveExporter() {
        if (!busy.compareAndSet(false, true)) {
            activity.toastError("Uma operação já está em andamento.");
            return false;
        }
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT_TREE);
        activity.startActivityForResult(intent, REQUEST_CODE_EXPORT_SAVES);
        return true;
    }

    public boolean openSaveImporter() {
        if (!busy.compareAndSet(false, true)) {
            activity.toastError("Uma operação já está em andamento.");
            return false;
        }
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT_TREE);
        activity.startActivityForResult(intent, REQUEST_CODE_IMPORT_SAVES);
        return true;
    }

    public boolean onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode != REQUEST_CODE_EXPORT_SAVES && requestCode != REQUEST_CODE_IMPORT_SAVES) {
            return false;
        }

        if (resultCode != Activity.RESULT_OK || data == null || data.getData() == null) {
            busy.set(false);
            activity.onImportCancelled();
            return true;
        }

        Uri treeUri = data.getData();

        if (requestCode == REQUEST_CODE_EXPORT_SAVES) {
            new Thread(() -> runExportSaves(treeUri), "SaveData-export").start();
        } else {
            new Thread(() -> runImportSaves(treeUri), "SaveData-import").start();
        }
        return true;
    }

    private void runExportSaves(Uri treeUri) {
        try {
            File savesDir = new File(activity.getExternalFilesDir(null), "saves");

            if (!savesDir.exists() || !savesDir.isDirectory()) {
                activity.toastError("A pasta de saves interna não foi encontrada.");
                return;
            }

            // only regular files, ignores subdirectories for progress count
            File[] files = savesDir.listFiles(File::isFile);
            if (files == null || files.length == 0) {
                activity.toastError("Não há nenhum arquivo de save para exportar.");
                return;
            }

            activity.updateImportProgress(0, "Iniciando exportação...");
            String treeId = DocumentsContract.getTreeDocumentId(treeUri);
            Uri rootDocUri = DocumentsContract.buildDocumentUriUsingTree(treeUri, treeId);

            String packageName = activity.getPackageName();
            Uri finalDestinationUri = rootDocUri;

            Uri packageFolderUri = DocumentsContract.createDocument(
                    activity.getContentResolver(), rootDocUri, DocumentsContract.Document.MIME_TYPE_DIR, packageName);

            if (packageFolderUri != null) {
                Uri filesFolderUri = DocumentsContract.createDocument(
                        activity.getContentResolver(), packageFolderUri, DocumentsContract.Document.MIME_TYPE_DIR, "files");
                if (filesFolderUri != null) {
                    Uri savesFolderUri = DocumentsContract.createDocument(
                            activity.getContentResolver(), filesFolderUri, DocumentsContract.Document.MIME_TYPE_DIR, "saves");
                    if (savesFolderUri != null) finalDestinationUri = savesFolderUri;
                    else finalDestinationUri = filesFolderUri;
                } else finalDestinationUri = packageFolderUri;
            }

            int totalFiles = files.length;
            int currentFileIndex = 0;

            for (File file : files) {
                activity.updateImportProgress((int) (100L * currentFileIndex / totalFiles), "Exportando: " + file.getName());
                Uri newFileUri = DocumentsContract.createDocument(
                        activity.getContentResolver(), finalDestinationUri, "application/octet-stream", file.getName());

                if (newFileUri != null) {
                    try (FileInputStream in = new FileInputStream(file);
                         ParcelFileDescriptor pfd = activity.getContentResolver().openFileDescriptor(newFileUri, "w");
                         FileOutputStream out = new FileOutputStream(pfd.getFileDescriptor())) {
                        byte[] buffer = new byte[64 * 1024];
                        int bytesRead;
                        while ((bytesRead = in.read(buffer)) != -1) {
                            out.write(buffer, 0, bytesRead);
                        }
                    }
                }
                currentFileIndex++;
            }

            activity.updateImportProgress(100, "Done");
            activity.toastMessage("Backup concluído com sucesso!");

        } catch (Exception e) {
            Log.e(TAG, "Erro crítico ao exportar a estrutura de saves", e);
            activity.updateImportProgress(-1, "Erro na exportação");
            activity.toastError("Falha ao exportar os saves.");
        } finally {
            busy.set(false);
        }
    }

    private void runImportSaves(Uri treeUri) {
        File tempDir = new File(activity.getExternalFilesDir(null), "saves_import_tmp");
        try {
            activity.updateImportProgress(0, "Verificando pasta...");

            String treeId = DocumentsContract.getTreeDocumentId(treeUri);
            Uri docUri = DocumentsContract.buildDocumentUriUsingTree(treeUri, treeId);

            try (Cursor cursor = activity.getContentResolver().query(docUri,
                    new String[]{DocumentsContract.Document.COLUMN_DISPLAY_NAME}, null, null, null)) {

                if (cursor == null || !cursor.moveToFirst()) {
                    Log.e(TAG, "Não foi possível verificar o nome da pasta selecionada.");
                    activity.updateImportProgress(-1, "Pasta inválida");
                    activity.toastError("Erro: Não foi possível verificar a pasta selecionada.");
                    return;
                }

                String folderName = cursor.getString(0);
                if (folderName == null || !folderName.equalsIgnoreCase("saves")) {
                    Log.e(TAG, "Tentativa de importar pasta inválida: " + folderName);
                    activity.updateImportProgress(-1, "Pasta inválida");
                    activity.toastError("Erro: Selecione a pasta 'saves' do seu backup!");
                    return;
                }
            }

            activity.updateImportProgress(0, "Preparando ambiente...");

            // copia para pasta temporária — saves original fica intacto em caso de falha
            deleteDir(tempDir);
            tempDir.mkdirs();

            Uri childrenUri = DocumentsContract.buildChildDocumentsUriUsingTree(treeUri, treeId);

            try (Cursor cursor = activity.getContentResolver().query(childrenUri,
                    new String[]{DocumentsContract.Document.COLUMN_DOCUMENT_ID, DocumentsContract.Document.COLUMN_DISPLAY_NAME},
                    null, null, null)) {

                if (cursor == null || cursor.getCount() == 0) {
                    Log.e(TAG, "Pasta selecionada está vazia ou inacessível.");
                    activity.updateImportProgress(-1, "Pasta vazia ou inacessível");
                    activity.toastError("Erro: Nenhum arquivo encontrado na pasta.");
                    return;
                }

                int totalFiles = cursor.getCount();
                int currentFileIndex = 0;

                while (cursor.moveToNext()) {
                    String docId = cursor.getString(0);
                    String displayName = cursor.getString(1);

                    Uri fileDocUri = DocumentsContract.buildDocumentUriUsingTree(treeUri, docId);
                    File destFile = new File(tempDir, displayName);

                    activity.updateImportProgress((int) (100L * currentFileIndex / totalFiles), "Restaurando: " + displayName);

                    try (InputStream in = activity.getContentResolver().openInputStream(fileDocUri);
                         FileOutputStream out = new FileOutputStream(destFile)) {
                        byte[] buffer = new byte[64 * 1024];
                        int read;
                        while ((read = in.read(buffer)) != -1) {
                            out.write(buffer, 0, read);
                        }
                    }
                    currentFileIndex++;
                }
            }

            // cópia completa — substitui saves pelo conteúdo do temp
            File savesDir = new File(activity.getExternalFilesDir(null), "saves");
            deleteDir(savesDir);
            savesDir.mkdirs();

            File[] newFiles = tempDir.listFiles();
            if (newFiles != null) {
                for (File f : newFiles) {
                    f.renameTo(new File(savesDir, f.getName()));
                }
            }

            activity.updateImportProgress(100, "Done");
            activity.toastMessage("Saves restaurados! O jogo será reiniciado.");

        } catch (Exception e) {
            Log.e(TAG, "Erro crítico ao importar os saves", e);
            activity.updateImportProgress(-1, "Erro na restauração");
            activity.toastError("Falha ao restaurar os saves.");
        } finally {
            deleteDir(tempDir);
            busy.set(false);
        }
    }

    private void deleteDir(File dir) {
        if (dir == null || !dir.exists()) return;
        File[] files = dir.listFiles();
        if (files != null) {
            for (File f : files) {
                if (f.isFile()) f.delete();
            }
        }
        dir.delete();
    }
}