package org.renpy.iap;

import java.util.HashSet;
import java.util.Map;

import com.amazon.device.iap.PurchasingListener;
import com.amazon.device.iap.PurchasingService;
import com.amazon.device.iap.model.Product;
import com.amazon.device.iap.model.ProductDataResponse;
import com.amazon.device.iap.model.PurchaseResponse;
import com.amazon.device.iap.model.PurchaseUpdatesResponse;
import com.amazon.device.iap.model.Receipt;
import com.amazon.device.iap.model.UserDataResponse;
import com.amazon.device.iap.model.FulfillmentResult;

import android.app.Activity;

public class AmazonStore extends Store implements PurchasingListener {

    Activity activity = null;

    boolean finished = true;


    public AmazonStore(Activity activity) {
        this.activity = activity;
        PurchasingService.registerListener(activity.getApplicationContext(), this);
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
        return "amazon";
    }

    @Override
    public void updatePrices() {
        HashSet<String> skuset = new HashSet<String>(skus);

        finished = false;
        PurchasingService.getProductData(skuset);
    }

    @Override
    public void restorePurchases() {
        finished = false;
        PurchasingService.getPurchaseUpdates(true);
    }

    @Override
    public void beginPurchase(String sku) {
        finished = false;
        PurchasingService.purchase(sku);
    }


    @Override
    public void onUserDataResponse(final UserDataResponse response) {
    }

    @Override
    public void onPurchaseUpdatesResponse(final PurchaseUpdatesResponse response) {
        if (response.getRequestStatus() != PurchaseUpdatesResponse.RequestStatus.SUCCESSFUL) {
            finished = true;
            return;
        }

        for (Receipt r : response.getReceipts()) {
            if (! r.isCanceled()) {
                purchased.add(r.getSku());
            }
        }

        if (response.hasMore()) {
            PurchasingService.getPurchaseUpdates(false);
        } else {
            finished = true;
        }

    }

    @Override
    public void onPurchaseResponse(final PurchaseResponse response) {
        if (response.getRequestStatus() != PurchaseResponse.RequestStatus.SUCCESSFUL) {
            finished = true;
            return;
        }

        purchased.add(response.getReceipt().getSku());

        PurchasingService.notifyFulfillment(response.getReceipt().getReceiptId(), FulfillmentResult.FULFILLED);

        finished = true;
    }

    @Override
    public void onProductDataResponse(ProductDataResponse response) {
        if (response.getRequestStatus() == ProductDataResponse.RequestStatus.SUCCESSFUL) {
            final Map<String, Product> products = response.getProductData();
            for (final String key : products.keySet()) {
              Product product = products.get(key);
              prices.put(product.getSku(), product.getPrice());
            }
        }

        finished = true;
    }

}
