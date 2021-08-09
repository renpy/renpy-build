package org.renpy.androidtest;

import java.util.Collections;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import com.google.android.play.core.assetpacks.*;
// import com.google.android.play.core.assetpacks.AssetPackManager;
// import com.google.android.play.core.assetpacks.AssetPackLocation;

public class MainActivity extends AppCompatActivity implements AssetPackStateUpdateListener {

    AssetPackManager mAssetPackManager = null;


    public void onStateUpdate(AssetPackState assetPackState) {
        // AssetPackManager assetPackManager = AssetPackManagerFactory.getInstance(this);
        // AssetPackLocation ff1 = assetPackManager.getPackLocation("ff1");

        Log.i("androidtest", "name = " + assetPackState.name());
        Log.i("androidtest", "status = " + assetPackState.status());


        AssetPackLocation ff1 = mAssetPackManager.getPackLocation("ff1");

        if (ff1 == null) {
            Log.i("androidtest", "ff1 == null"); 
        } else {
            Log.i("androidtest", "ff1 == " + ff1.assetsPath());
        }





    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        Log.i("androidtest", "onCreate");

        mAssetPackManager = AssetPackManagerFactory.getInstance(this);

        mAssetPackManager.registerListener(this);
        mAssetPackManager.fetch(Collections.singletonList("ff1"));


        AssetPackLocation ff1 = mAssetPackManager.getPackLocation("ff1");

        if (ff1 == null) {
            Log.i("androidtest", "ff1 == null"); 
        } else {
            Log.i("androidtest", "ff1 == " + ff1.assetsPath());
        }


    
    }
}