#include <stdio.h>

@import UIKit;
@import AVFoundation;

@interface VideoPlayerView : UIView
@property (nonatomic) AVPlayer *player;
@end

@interface VideoPlayer : NSObject {
    UIWindow *window;
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

@end


@implementation VideoPlayer

- (id) initWithFile: (char *) fn {
    self = [ super init ];
    if (!self) {
        return nil;
    }

    window = [[ UIApplication sharedApplication] keyWindow];

    NSString *string = [NSString stringWithUTF8String: fn];
    NSURL *url = [ NSURL fileURLWithPath: string ];
    player = [ AVPlayer playerWithURL: url ];

    vpv = [[ VideoPlayerView alloc ] init ];
    
    [ vpv setPlayer: player ];
    vpv.opaque = YES;
    vpv.backgroundColor = [ UIColor blackColor ];
    
    vpv.frame = window.frame;

    
    
    [ [ [ window subviews ]  objectAtIndex: 0 ] addSubview: vpv];
    
    printf("Initialized VP with file %s\n", fn);

    [ player play ];

    playing = YES;
    paused = NO;
    
    return self;
}

- (int) isPlaying {
    if (! playing) {
        return NO;
    }
    
    if (playing && paused) {
        return YES;
    }
    
    vpv.frame = window.frame;
    
    if (! player.rate) {
        [ self stop ];
    } else if (player.error) {
        [ self stop ];
    }
    
    return playing;
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
