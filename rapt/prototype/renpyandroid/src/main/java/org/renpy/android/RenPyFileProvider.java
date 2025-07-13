package org.renpy.android;

import androidx.core.content.FileProvider;

public class RenPyFileProvider extends FileProvider {
    public RenPyFileProvider() {
        super(R.xml.file_paths);
    }
}
