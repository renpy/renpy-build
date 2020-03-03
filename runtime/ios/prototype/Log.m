@import Foundation;

@interface Log : NSObject
+ (void) log: (char *) s;
@end

@implementation Log

+ (void) log: (char *) s {
    NSLog(@"%s", s);
}

@end
