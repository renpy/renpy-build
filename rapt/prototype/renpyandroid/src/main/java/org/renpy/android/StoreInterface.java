package org.renpy.android;

import android.content.Intent;

public interface StoreInterface {
    public void destroy();
    public boolean onActivityResult(int requestCode, int resultCode, Intent intent);
}
