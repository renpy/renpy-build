Tars
====

This directory is for source files too big (or too poorly licensed) to go
into github. Right now, it needs:

Xcode
-----

* MacOSX12.3.sdk.tar.bz2

Created as described at https://github.com/tpoechtrager/osxcross#packaging-the-sdk .
This old version is required to ensure that Ren'Py runs on older versions of
macOS.

* iPhoneOS.sdk.tar.gz
* iPhoneSimulator.sdk.tar.gz

Run ./ios_toolchains.sh /path/to/Xcode.app
to package the device and simulator SDKs. The current iOS build uses SDK 27.1
with an iOS 15.0 minimum deployment target.

Android NDK
-----------

* android-ndk-r27c-linux.zip

Downloaded from https://developer.android.com/ndk/downloads .

Live2D Cubism SDK for Native
----------------------------

* CubismSDKforNative-5-r.5.zip

Downloaded from https://www.live2d.com/en/download/cubism-sdk/ .

Steamworks SDK
--------------

* steamworks_sdk_160.zip

Downloaded from https://partner.steamgames.com/doc/sdk , which is only
available to Steam partners. Ren'Py will build without the Steamworks
SDK.
