#!/bin/bash

# Generate toolchain tars from $XCODE
# Based on  https://github.com/tpoechtrager/cctools-port/tree/master/usage_examples/ios_toolchain

set -euo pipefail


if [[ $# -lt 1 ]]; then
	echo "usage: $0 /path/to/Xcode.app" >&2
	exit 1
fi

XCODE="$1"

copy_libcxx_headers() {
	local sdk_root="$1"
	local sdk_name="$2"

	local sdk_cpp_dir="${sdk_root}/usr/include/c++"
	local sdk_cpp_v1_dir="${sdk_cpp_dir}/v1"
	local toolchain_cpp_v1_dir="$XCODE/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1"

	# Newer Xcode SDKs may already contain libc++ headers.
	if [[ -d "$sdk_cpp_v1_dir" ]]; then
		return
	fi

	# Older Xcode layouts keep libc++ headers in the default toolchain.
	if [[ -d "$toolchain_cpp_v1_dir" ]]; then
		mkdir -p "$sdk_cpp_dir"
		cp -r "$toolchain_cpp_v1_dir" "$sdk_cpp_dir"
		return
	fi

	echo "error: could not locate libc++ headers for ${sdk_name}" >&2
	echo "checked: $sdk_cpp_v1_dir" >&2
	echo "checked: $toolchain_cpp_v1_dir" >&2
	exit 1
}

SDK_DIR="$XCODE/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs"
SDK="iPhoneOS.sdk"
cp -r "$SDK_DIR/$SDK" "/tmp/$SDK" 1>/dev/null
copy_libcxx_headers "/tmp/$SDK" "$SDK"
pushd /tmp
tar -cvzf "$SDK.tar.gz" "$SDK"
rm -rf "$SDK"
popd

mv "/tmp/$SDK.tar.gz" .

SDK_DIR="$XCODE/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs"
SDK="iPhoneSimulator.sdk"
cp -r "$SDK_DIR/$SDK" "/tmp/$SDK" 1>/dev/null
copy_libcxx_headers "/tmp/$SDK" "$SDK"
pushd /tmp
tar -cvzf "$SDK.tar.gz" "$SDK"
rm -rf "$SDK"
popd

mv "/tmp/$SDK.tar.gz" .
