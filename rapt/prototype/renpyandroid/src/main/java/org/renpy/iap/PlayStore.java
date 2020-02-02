package org.renpy.iap;

import java.util.ArrayList;

import org.json.JSONException;
import org.json.JSONObject;

import android.app.Activity;
import android.app.PendingIntent;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.os.RemoteException;
import android.util.Log;

import com.android.vending.billing.IInAppBillingService;

public class PlayStore extends Store {

    /** True if we're finished with what we're trying to do. */
    boolean finished = true;

    /** The activity we're associated with. */
    Activity activity;

    /** The billing service. */
    IInAppBillingService service;

    /** The connection to the billing service. */
    ServiceConnection connection = new ServiceConnection() {
       @Override
       public void onServiceDisconnected(ComponentName name) {
           service = null;
       }

       @Override
       public void onServiceConnected(ComponentName name, IBinder binder) {
           service = IInAppBillingService.Stub.asInterface(binder);
       }
    };

    public PlayStore(Activity activity) {
        this.activity = activity;

        Intent serviceIntent = new Intent("com.android.vending.billing.InAppBillingService.BIND");
        serviceIntent.setPackage("com.android.vending");
        activity.bindService(serviceIntent, connection, Context.BIND_AUTO_CREATE);
    }

    @Override
    public void destroy() {
        if (service != null) {
            this.activity.unbindService(connection);
        }
    };

    @Override
    public boolean getFinished() {
        return finished;
    }

    @Override
    public String getStoreName() {
        return "play";
    }

    public boolean isBillingSupported() {
        if (service == null) {
            return false;
        }

        try {
            int response = service.isBillingSupported(3, activity.getPackageName(), "inapp");
            return response == 0; // RESULT_OK
        } catch (RemoteException e) {
            return false;
        }
    }

    public void updatePrices() {
        finished = false;

        new Thread() {
            public void run() {
                try {
                    Bundle querySkus = new Bundle();
                    querySkus.putStringArrayList("ITEM_ID_LIST", skus);

                    Bundle skuDetails = service.getSkuDetails(3, activity.getPackageName(), "inapp", querySkus);
                    int response = skuDetails.getInt("RESPONSE_CODE");

                    if (response == 0) {
                        ArrayList<String> responseList = skuDetails.getStringArrayList("DETAILS_LIST");

                        prices.clear();

                        for (String thisResponse : responseList) {
                            JSONObject object = new JSONObject(thisResponse);
                            String sku = object.getString("productId");
                            String price = object.getString("price");

                            Log.i("iap", "sku " + sku + " price " + price);
                            prices.put(sku, price);
                        }
                    }

                } catch (Exception e) {
                    Log.e("iap", "getSkuDetails failed.", e);
                }

                finished = true;
            }
        }.start();

    };

    @Override
    public void restorePurchases() {
        try {
            Bundle ownedItems = service.getPurchases(3, activity.getPackageName(), "inapp", null);

            int response = ownedItems.getInt("RESPONSE_CODE");

            if (response == 0) {
                ArrayList<String> ownedSkus = ownedItems.getStringArrayList("INAPP_PURCHASE_ITEM_LIST");

                purchased.clear();

                for (String s : ownedSkus) {
                    purchased.add(s);
                }
            }
        } catch (Exception e) {
            Log.e("iap", "restorePurchases failed.", e);
        }

        finished = true;
    }

    @Override
    public void beginPurchase(String sku) {
        try {
            finished = false;
            Bundle buyIntentBundle = service.getBuyIntent(3, activity.getPackageName(), sku, "inapp", "via renpy.iap");
            PendingIntent pendingIntent = buyIntentBundle.getParcelable("BUY_INTENT");

            activity.startIntentSenderForResult(
                    pendingIntent.getIntentSender(),
                    1001,
                    new Intent(),
                    Integer.valueOf(0),
                    Integer.valueOf(0),
                    Integer.valueOf(0));


        } catch (Exception e) {
            finished = true;
            Log.e("iap", "beginPurchase failed.", e);
        }
    }

    @Override
    public boolean onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == 1001) {
            try {

                int responseCode = data.getIntExtra("RESPONSE_CODE", 0);
                String purchaseData = data.getStringExtra("INAPP_PURCHASE_DATA");
                // String dataSignature = data.getStringExtra("INAPP_DATA_SIGNATURE");

                Log.i("iap", "resultCode = " + resultCode + ", responseCode = " + responseCode);

                if (resultCode == Activity.RESULT_OK && (responseCode == 0 || responseCode == 7)) {
                    try {
                        JSONObject jo = new JSONObject(purchaseData);
                        String sku = jo.getString("productId");
                        purchased.add(sku);
                    }  catch (JSONException e) {
                        Log.e("iap", "Failed to parse purchase data.", e);
                    }
                }

            } finally {
                finished = true;
            }

            return true;
        }


        return false;
    }



}
