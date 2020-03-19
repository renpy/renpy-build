#!/bin/bash

set -ex

pushd /Volumes/shared/ab/renpy-build/renios/prototype
xcodebuild -project prototype.xcodeproj/ -scheme prototype -configuration Debug -destination 'platform=iOS Simulator,name=iPhone 11 Pro Max,OS=13.3'
xcrun simctl install booted ~/Library/Developer/Xcode/DerivedData/prototype-ftosscwgctqkhgaylgxdbpdvtkdk/Build/Products/Debug-iphonesimulator/prototype.app
