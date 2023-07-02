#import <Foundation/Foundation.h>

@import StoreKit;

@interface IAPHelper : NSObject <SKProductsRequestDelegate, SKPaymentTransactionObserver>

// An array of product identifier NSStrings. This is set when we're first constructed.
@property NSArray *productIdentifiers;

// A map from a product identifier NSString to the corresponding project.
@property NSMutableDictionary *products;

// 1 if the queue is initialized, 0 otherwise.
@property int initialized_queue;

// 1 if an operation is in progress. 0 if no operation is in progress.
@property int validated;

// 1 if an operation is in progress. 0 if no operation is in progress.
@property int finished;

// The set of identifiers for purchased products.
@property NSMutableSet *purchased;

// The set of identifiers for deferred products.
@property NSMutableSet *deferred;

// The title to use for the dialog window.
@property NSString *dialogTitle;

- (id) init;
- (void) initQueue;
- (BOOL) canMakePayments;
- (void) validateProductIdentifiersInBackground;
- (void) validateProductIdentifiers;
- (void) beginPurchase: (NSString *) identifier;
- (BOOL) hasPurchased: (NSString *) identifier;
- (BOOL) hasPurchasedConsumable: (NSString *) identifier;
- (BOOL) isDeferred: (NSString *) identifier;
- (NSString *) formatPrice: (NSString *) identifier;
- (void) requestReview;
@end;


@implementation IAPHelper

UIAlertController *alert;

- (id) init {
    self = [ super init ];
    self.products = [ [ NSMutableDictionary alloc] init];
    self.purchased = [ [ NSMutableSet alloc ] init ];
    self.deferred = [ [ NSMutableSet alloc ] init ];
    self.validated = 0;
    self.finished = 1;
    self.initialized_queue = 0;
    self.dialogTitle = @"Contacting App Store\nPlease Wait...";

    return self;
}

- (void) initQueue {
    if (self.initialized_queue) {
        return;
    }

    [[SKPaymentQueue defaultQueue] addTransactionObserver: self];

    self.initialized_queue = 1;

    return;
}

- (BOOL) canMakePayments {
    [self initQueue];
    return [SKPaymentQueue canMakePayments];
}

- (void) validateProductIdentifiers {

    printf("Starting validation.\n");

    if (self.validated) {
        printf("Already validated.\n");
        self.finished = 1;
        return;
    }

    [self showDialog];

    SKProductsRequest *productsRequest = [[SKProductsRequest alloc]
                                          initWithProductIdentifiers:[NSSet setWithArray: self.productIdentifiers]];
    self.finished = 0;
    productsRequest.delegate = self;
    [productsRequest start];

}

- (void) validateProductIdentifiersInBackground {

    SKProductsRequest *productsRequest = [[SKProductsRequest alloc]
                                          initWithProductIdentifiers:[NSSet setWithArray: self.productIdentifiers]];
    self.validated = 0;
    productsRequest.delegate = self;
    [productsRequest start];

}

- (void)productsRequest:(SKProductsRequest *)request didReceiveResponse:(SKProductsResponse *)response {
    for (SKProduct *prod in response.products) {
        [ self.products setObject: prod forKey: prod.productIdentifier ];
    }

    [self hideDialog];

    self.validated = 1;
    self.finished = 1;

    printf("Validated product identifiers.\n");
}

- (void) showDialog {

    if (alert != nil) {
        return;
    }

    alert = [UIAlertController
             alertControllerWithTitle:self.dialogTitle
             message:nil
             preferredStyle:UIAlertControllerStyleAlert ];

    UIActivityIndicatorView *indicator = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle:UIActivityIndicatorViewStyleLarge];

    // Adjust the indicator so it is up a few pixels from the bottom of the alert

    indicator.center = CGPointMake(alert.view.bounds.size.width / 2, alert.view.bounds.size.height - 50);
    [indicator startAnimating];

    [alert.view addSubview: indicator];

    #pragma clang diagnostic push
    #pragma clang diagnostic ignored "-Wdeprecated"
    [UIApplication.sharedApplication.keyWindow.rootViewController presentViewController:alert animated:YES completion:nil];
    #pragma clang diagnostic pop

}

- (void) hideDialog {
    if (alert != nil) {
        [alert dismissViewControllerAnimated:YES completion:nil];
        alert = nil;
    }
}

- (void) beginPurchase: (NSString *) identifier {
    [self initQueue];

    SKProduct *product = [ self.products objectForKey: identifier ];

    if (product == nil) {
        return;
    }

    [self showDialog];

    self.finished = 0;

    SKMutablePayment *payment = [ SKMutablePayment paymentWithProduct: product ];
    payment.quantity = 1;

    [[SKPaymentQueue defaultQueue] addPayment: payment];

}

- (void) restorePurchases {
    [self showDialog];
    [self initQueue];

    self.finished = 0;

    [[SKPaymentQueue defaultQueue] restoreCompletedTransactions ];
    printf("Restore started.\n");
}

- (void) paymentQueue: (SKPaymentQueue *) queue updatedTransactions: (NSArray *) transactions {
    for (SKPaymentTransaction *t in transactions) {
        NSString *identifier = t.payment.productIdentifier;

        switch (t.transactionState) {
            case SKPaymentTransactionStatePurchased:
                printf("Purchased %s\n", [ identifier UTF8String ]);
                [ self.deferred removeObject: identifier ];
                [ self.purchased addObject: identifier ];
                [ [ SKPaymentQueue defaultQueue] finishTransaction: t ];
                [self hideDialog];
                self.finished = 1;
                break;

            case SKPaymentTransactionStateFailed:
                printf("Failed %s\n", [ identifier UTF8String ]);
                [ [ SKPaymentQueue defaultQueue] finishTransaction: t ];
                [self hideDialog];
                self.finished = 1;
                break;

            case SKPaymentTransactionStateRestored:
                printf("Restored %s\n", [ identifier UTF8String ]);
                [ self.deferred removeObject: identifier ];
                [ self.purchased addObject: identifier ];
                [ [ SKPaymentQueue defaultQueue] finishTransaction: t ];

                break;

            case SKPaymentTransactionStatePurchasing:
                printf("Purchasing %s\n", [ identifier UTF8String ]);
                break;

            case SKPaymentTransactionStateDeferred:
                printf("Deferred %s\n", [ identifier UTF8String ]);
                [ self.deferred addObject: identifier ];
                [self hideDialog];
                self.finished = 1;
                break;
        }
    }
}

- (void) paymentQueue: (SKPaymentQueue *)queue restoreCompletedTransactionsFailedWithError: (NSError *) error {
    printf("Restore failed with error.\n");
    [self hideDialog];
    self.finished = 1;
}

- (void) paymentQueueRestoreCompletedTransactionsFinished: (SKPaymentQueue *) queue {
    printf("Restore completed.\n");
    [self hideDialog];
    self.finished = 1;
}


- (BOOL) hasPurchased: (NSString *) identifier {
    return [ self.purchased member: identifier ] != nil;
}

// this checks for the purchase and then erases it from the purchased array to prevent returning
// true even if the subsequent purchase was cancelled

- (BOOL) hasPurchasedConsumable: (NSString *) identifier {
    bool res = [ self.purchased member: identifier ] != nil;
    [self.purchased removeObject: identifier];
    return res;
}

- (BOOL) isDeferred: (NSString *) identifier {
    return [ self.deferred member: identifier ] != nil;
}

- (NSString *) formatPrice: (NSString *) identifier {
    SKProduct *product = [ self.products objectForKey: identifier ];

    if (product == nil) {
        return nil;
    }

    NSNumberFormatter *numberFormatter = [[NSNumberFormatter alloc] init];
    [numberFormatter setFormatterBehavior:NSNumberFormatterBehavior10_4];
    [numberFormatter setNumberStyle:NSNumberFormatterCurrencyStyle];
    [numberFormatter setLocale:product.priceLocale];
    return [numberFormatter stringFromNumber:product.price];
}

- (void) requestReview {
    [SKStoreReviewController requestReview];
}

@end
