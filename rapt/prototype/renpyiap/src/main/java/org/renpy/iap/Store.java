package org.renpy.iap;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;

import org.renpy.android.StoreInterface;
import org.renpy.android.PythonSDLActivity;

public class Store implements StoreInterface {

    static public Store store = null;

    static public void create(PythonSDLActivity activity) {

        String storeName = org.renpy.android.Constants.store;

        if (storeName.equals("all")) {
            PackageManager pkgManager = activity.getPackageManager();
            String installerPackageName = pkgManager.getInstallerPackageName(activity.getPackageName());

            if (installerPackageName == null) {
                 if (android.os.Build.MANUFACTURER.startsWith("Amazon")) {
                     storeName = "amazon";
                 } else {
                     storeName = "play";
                 }

            } else if (installerPackageName.startsWith("com.amazon")) {
                storeName = "amazon";
            } else {
                storeName = "play";
            }

        }

        android.util.Log.e("python", "Selecting the " + storeName + " store.");

        if (storeName.equals("play")) {
            store = new PlayStore(activity);
        } else if (storeName.equals("amazon")) {
            store = new AmazonStore(activity);
        } else {
            store = new Store();
        }

        activity.mStore = store;
    }

    static public Store getStore() {
        return store;
    }

    public void destroy() {
    }

    public boolean onActivityResult(int requestCode, int resultCode, Intent intent) {
        return false;
    }

    public boolean getFinished() {
        return true;
    }

    public String getStoreName() {
        return "none";
    }

    public ArrayList<String> skus = new ArrayList<String>();
    public HashMap<String, String> prices = new HashMap<String, String>();

    public void clearSKUs() {
        skus.clear();
    }

    public void addSKU(String sku) {
        skus.add(sku);
    }

    public void updatePrices() {
        return;
    }

    public String getPrice(String sku) {
        return prices.get(sku);
    }

    HashSet<String> purchased = new HashSet<String>();

    public boolean hasPurchased(String sku) {
       return purchased.contains(sku);
    }

    public void restorePurchases() {
    }

    public void beginPurchase(String sku) {
    }

    public boolean requestReview() {
        return false;
    }

}
