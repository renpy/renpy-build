/*
 * Copyright (C) 2012 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.google.android.vending.expansion.downloader.impl;

import com.google.android.vending.expansion.downloader.Helpers;

/**
 * Representation of information about an individual download from the database.
 */
public class DownloadInfo {
    public String mUri;
    public final int mIndex;
    public final String mFileName;
    public String mETag;
    public long mTotalBytes;
    public long mCurrentBytes;
    public long mLastMod;
    public int mStatus;
    public int mControl;
    public int mNumFailed;
    public int mRetryAfter;
    public int mRedirectCount;

    boolean mInitialized;

    public int mFuzz;

    public DownloadInfo(int index, String fileName, String pkg) {
        mFuzz = Helpers.sRandom.nextInt(1001);
        mFileName = fileName;
        mIndex = index;
    }

    public void resetDownload() {
        mCurrentBytes = 0;
        mETag = "";
        mLastMod = 0;
        mStatus = 0;
        mControl = 0;
        mNumFailed = 0;
        mRetryAfter = 0;
        mRedirectCount = 0;
    }
}
