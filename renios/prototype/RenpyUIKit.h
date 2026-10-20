#ifndef RENPY_UIKIT_H
#define RENPY_UIKIT_H

@import UIKit;

static inline UIWindow *RenpyUIKitGetWindow(void)
{
    if (![NSThread isMainThread]) {
        NSLog(@"Ren'Py native UI must be called on the main thread.");
        return nil;
    }

    UISceneActivationState states[] = {
        UISceneActivationStateForegroundActive,
        UISceneActivationStateForegroundInactive,
    };

    for (NSUInteger i = 0; i < sizeof(states) / sizeof(states[0]); ++i) {
        UIWindow *fallback = nil;

        for (UIScene *scene in UIApplication.sharedApplication.connectedScenes) {
            if (![scene isKindOfClass:UIWindowScene.class] || scene.activationState != states[i]) {
                continue;
            }

            for (UIWindow *window in ((UIWindowScene *)scene).windows) {
                if (window.hidden || window.alpha == 0 || window.windowLevel != UIWindowLevelNormal || !window.rootViewController) {
                    continue;
                }

                if (window.isKeyWindow) {
                    return window;
                }

                if (!fallback) {
                    fallback = window;
                }
            }
        }

        if (fallback) {
            return fallback;
        }
    }

    NSLog(@"Ren'Py native UI has no foreground application window.");
    return nil;
}

static inline UIViewController *RenpyUIKitGetPresenter(UIWindow *window)
{
    UIViewController *controller = window.rootViewController;

    while (controller) {
        if (controller.presentedViewController) {
            controller = controller.presentedViewController;
        } else if ([controller isKindOfClass:UINavigationController.class] &&
                   ((UINavigationController *)controller).visibleViewController) {
            controller = ((UINavigationController *)controller).visibleViewController;
        } else if ([controller isKindOfClass:UITabBarController.class] &&
                   ((UITabBarController *)controller).selectedViewController) {
            controller = ((UITabBarController *)controller).selectedViewController;
        } else {
            return controller;
        }
    }

    return nil;
}

#endif
