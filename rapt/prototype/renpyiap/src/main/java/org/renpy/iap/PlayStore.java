package org.renpy.iap;

import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Objects;

import android.app.Activity;
import androidx.annotation.NonNull;
import android.util.Log;

import com.android.billingclient.api.*;

import com.google.android.play.core.review.ReviewManager;
import com.google.android.play.core.review.ReviewManagerFactory;
import com.google.android.play.core.review.ReviewInfo;
import com.google.android.gms.tasks.Task;


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

    /* A map from sku to ProductDetails object. */
    private HashMap<String, ProductDetails> productDetailsMap = new HashMap<>();

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

            for (String sku : purchase.getProducts()) {
                purchased.add(sku);
            }
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

            List<QueryProductDetailsParams.Product> products = new ArrayList<QueryProductDetailsParams.Product>();

            for (String s : skus) {
                Log.i("iap", "Trying to get prices for " + s);
                products.add(QueryProductDetailsParams.Product.newBuilder().setProductId(s).setProductType(BillingClient.ProductType.INAPP).build());
            }

            QueryProductDetailsParams.Builder params = QueryProductDetailsParams.newBuilder();
            params.setProductList(products);

            billingClient.queryProductDetailsAsync(
                params.build(),
                new ProductDetailsResponseListener() {
                    @Override
                    public void onProductDetailsResponse(@NonNull BillingResult billingResult, List<ProductDetails> productDetailsList) {
                        if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                            prices.clear();

                            for (ProductDetails p : productDetailsList) {
                                String price = p.getOneTimePurchaseOfferDetails().getFormattedPrice();
                                Log.i("iap", "Got price id=" + p.getProductId() + " price=" + price);
                                prices.put(p.getProductId(), price);
                                productDetailsMap.put(p.getProductId(), p);
                            }

                            finished = true;
                        }
                    }
                }
            );

        } catch (Exception e) {
            finished = true;
            Log.e("iap", "updatePrices failed.", e);
        }
    }

    @Override
    public void restorePurchases() {
        try {

            billingClient.queryPurchasesAsync(
                QueryPurchasesParams.newBuilder().setProductType(BillingClient.ProductType.INAPP).build(),
                new PurchasesResponseListener() {
                    @Override
                    public void onQueryPurchasesResponse(@NonNull BillingResult billingResult, List<Purchase> purchases) {
                        if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK) {
                            for (Purchase p : purchases) {
                                handlePurchase(p);
                            }
                        }

                        finished = true;
                    }
                }
            );


        } catch (Exception e) {
            Log.e("iap", "restorePurchases failed.", e);
            finished = true;
        }
    }

    @Override
    public void beginPurchase(String sku) {
        try {
            finished = false;

            Log.i("iap", "beginPurchase " + sku);

            ArrayList<BillingFlowParams.ProductDetailsParams> productDetailsParamsList = new ArrayList<>();
            productDetailsParamsList.add(BillingFlowParams.ProductDetailsParams.newBuilder().setProductDetails(productDetailsMap.get(sku)).build());
            BillingFlowParams billingFlowParams = BillingFlowParams.newBuilder().setProductDetailsParamsList(productDetailsParamsList).build();

            int responseCode = billingClient.launchBillingFlow(activity, billingFlowParams).getResponseCode();

            if (responseCode != BillingClient.BillingResponseCode.OK) {
                finished = true;
            }

        } catch (Exception e) {
            finished = true;
            Log.e("iap", "beginPurchase failed.", e);
        }
    }

    @Override
    public boolean requestReview() {
        ReviewManager manager = ReviewManagerFactory.create(activity);
        Task<ReviewInfo> request = manager.requestReviewFlow();
        request.addOnCompleteListener(task -> {
            if (task.isSuccessful()) {
                ReviewInfo reviewInfo = task.getResult();
                manager.launchReviewFlow(activity, reviewInfo);
            }
        });

        return true;
    }
}
