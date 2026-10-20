#include <stdio.h>
#import "RenpyUIKit.h"

@import UIKit;
@import AVFoundation;
@import Dispatch;

@interface VideoPlayerView : UIView
@property (nonatomic) AVPlayer *player;
@end

@interface VideoPlayer : NSObject {
    UIView *hostView;
    AVPlayer *player;
    VideoPlayerView *vpv;
    BOOL playing;
    BOOL paused;
}

- (id) initWithFile: (char *) fn;
- (int) isPlaying;
- (void) stop;
- (void) pause;
- (void) unpause;
- (void) periodic;

@end


@implementation VideoPlayer

- (id) initWithFile: (char *) fn {
    self = [ super init ];
    if (!self) {
        return nil;
    }

    UIWindow *window = RenpyUIKitGetWindow();
    hostView = window.rootViewController.view;
    if (!hostView) {
        NSLog(@"Unable to start video without a foreground game view.");
        return self;
    }

    NSString *string = [NSString stringWithUTF8String: fn];
    NSURL *url = [ NSURL fileURLWithPath: string ];
    player = [ AVPlayer playerWithURL: url ];

    vpv = [[ VideoPlayerView alloc ] init ];

    [ vpv setPlayer: player ];
    vpv.opaque = YES;
    vpv.backgroundColor = [ UIColor blackColor ];

    vpv.frame = hostView.bounds;
    vpv.autoresizingMask = UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight;

    [hostView addSubview:vpv];

    printf("Initialized VP with file %s\n", fn);

    [ player play ];

    playing = YES;
    paused = NO;

    return self;
}

- (int) isPlaying {
    return playing;
}

- (void) periodic {
    if (! playing) {
        return;
    }

    if (playing && paused) {
        return;
    }

    if (! player.rate) {
        [ self stop ];
    } else if (player.error) {
        [ self stop ];
    }

    return;
}

- (void) stop {
    [ player pause ];
    [ vpv removeFromSuperview ];
    playing = NO;
    paused = NO;

}

- (void) pause {
    [ player pause ];
    paused = YES;
}

- (void) unpause {
    if (!playing) {
        return;
    }

    [ player play ];
    paused = NO;
}

@end

@implementation VideoPlayerView
+ (Class)layerClass {
    return [AVPlayerLayer class];
}
- (AVPlayer*)player {
    return [(AVPlayerLayer *)[self layer] player];
}
- (void)setPlayer:(AVPlayer *)player {
    [(AVPlayerLayer *)[self layer] setPlayer:player];
}
@end
