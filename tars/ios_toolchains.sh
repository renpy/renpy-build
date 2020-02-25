#!/bin/bash

# Generate toolchain tars from $XCODE
# Based on  https://github.com/tpoechtrager/cctools-port/tree/master/usage_examples/ios_toolchain


XCODE="$1"

SDK=$(ls -l $XCODE/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs | grep " -> iPhoneOS.sdk" | head -n1 | awk '{print $9}')
cp -r $XCODE/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS.sdk /tmp/$SDK 1>/dev/null
cp -r $XCODE/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1 /tmp/$SDK/usr/include/c++ 1>/dev/null
pushd /tmp
tar -cvzf $SDK.tar.gz $SDK
rm -rf $SDK
popd

mv /tmp/$SDK.tar.gz .

SDK=$(ls -l $XCODE/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs | grep " -> iPhoneSimulator.sdk" | head -n1 | awk '{print $9}')
cp -r $XCODE/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk /tmp/$SDK 1>/dev/null
cp -r $XCODE/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1 /tmp/$SDK/usr/include/c++ 1>/dev/null
pushd /tmp
tar -cvzf $SDK.tar.gz $SDK
rm -rf $SDK
popd

mv /tmp/$SDK.tar.gz .
