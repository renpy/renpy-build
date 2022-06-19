package org.renpy.iap;

import java.util.HashMap;
import java.util.List;
import java.util.Objects;

import android.app.Activity;
import android.support.annotation.NonNull;
import android.util.Log;

import com.android.billingclient.api.*;


public class PlayStore extends Store {

    /**
     * True if we're finished with what we're trying to do.
     */
    boolean finished = true;

    /**
     * The activity we're associated with.
     */
    Activity activity;

    /* The billingClient object, if it exists. */
    private BillingClient billingClient = null;

    /* A map from sku to SkuDetails object. */
    private HashMap<String, SkuDetails> skuDetailsMap = new HashMap<>();

    public PlayStore(Activity activity) {
        this.activity = activity;

        final BillingClient bc = BillingClient.newBuilder(activity)
                .setListener(purchasesUpdatedListener)
                .enablePendingPurchases()
                .build();

        bc.startConnection(new BillingClientStateListener() {
            @Override
            public void onBillingSetupFinished(@NonNull BillingResult billingResult) {
                if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                    billingClient = bc;
                }
            }

            @Override
            public void onBillingServiceDisconnected() {
                billingClient = null;
            }
        });
    }

    private PurchasesUpdatedListener purchasesUpdatedListener = new PurchasesUpdatedListener() {
        @Override
        public void onPurchasesUpdated(BillingResult billingResult, List<Purchase> purchases) {
            if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                if (purchases != null) {
                    for (Purchase p : purchases) {
                        handlePurchase(p);
                    }
                }
            }

            finished = true;
        }
    };

    AcknowledgePurchaseResponseListener acknowledgePurchaseResponseListener = new AcknowledgePurchaseResponseListener() {
        @Override
        public void onAcknowledgePurchaseResponse(@NonNull BillingResult billingResult) {
        }
    };

    void handlePurchase(Purchase purchase) {
        if (purchase.getPurchaseState() == Purchase.PurchaseState.PURCHASED) {
            if (!purchase.isAcknowledged()) {
                AcknowledgePurchaseParams acknowledgePurchaseParams = AcknowledgePurchaseParams.newBuilder().setPurchaseToken(purchase.getPurchaseToken()).build();
                billingClient.acknowledgePurchase(acknowledgePurchaseParams, acknowledgePurchaseResponseListener);
            }

            purchased.add(purchase.getSku());
        }
    }


    @Override
    public void destroy() {
    }

    @Override
    public boolean getFinished() {
        return finished;
    }

    @Override
    public String getStoreName() {
        return "play";
    }


    @Override
    public void updatePrices() {
        try {

            finished = false;

            SkuDetailsParams.Builder params = SkuDetailsParams.newBuilder();
            params.setSkusList(skus).setType(BillingClient.SkuType.INAPP);

            for (String s : skus) {
                Log.i("iap", "Trying to get prices for " + s);
            }

            billingClient.querySkuDetailsAsync(params.build(),
                    new SkuDetailsResponseListener() {
                        @Override
                        public void onSkuDetailsResponse(@NonNull BillingResult billingResult, List<SkuDetails> skuDetailsList) {
                            if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                                prices.clear();

                                for (SkuDetails sku : skuDetailsList) {
                                    prices.put(sku.getSku(), sku.getPrice());
                                    skuDetailsMap.put(sku.getSku(), sku);
                                }

                                finished = true;
                            }
                        }
                    });

        } catch (Exception e) {
            finished = true;
            Log.e("iap", "updatePrices failed.", e);
        }
    }

    @Override
    public void restorePurchases() {
        try {

            Purchase.PurchasesResult pr = billingClient.queryPurchases(BillingClient.SkuType.INAPP);
            if (pr.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                if (pr.getPurchasesList() != null) {
                    for (Purchase p : pr.getPurchasesList()) {
                        handlePurchase(p);
                    }
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

            // Retrieve a value for "skuDetails" by calling querySkuDetailsAsync().
            BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder()
                    .setSkuDetails(Objects.requireNonNull(skuDetailsMap.get(sku)))
                    .build();

            int responseCode = billingClient.launchBillingFlow(activity, billingFlowParams).getResponseCode();

            if (responseCode != BillingClient.BillingResponseCode.OK) {
                finished = true;
            }

        } catch (Exception e) {
            finished = true;
            Log.e("iap", "beginPurchase failed.", e);
        }
    }
}
