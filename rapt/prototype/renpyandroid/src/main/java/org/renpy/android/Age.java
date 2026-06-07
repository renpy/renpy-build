package org.renpy.android;

import android.content.Context;
import android.util.Log;

import com.google.android.play.agesignals.AgeSignalsManager;
import com.google.android.play.agesignals.AgeSignalsManagerFactory;
import com.google.android.play.agesignals.AgeSignalsRequest;

public class Age {
    public static boolean requested = false;
    public static boolean inProgress = false;
    public static boolean valid = false;
    public static int ageLower = -1;
    public static int ageUpper = 150;

    /**
     * Causes an asynchronous request to the Android Age Signals API to update the age signals.
     */
    public static void update(Context context) {

        // Already made the request, so no need to do it again.
        if (requested) {
            return;
        }

        requested = true;
        inProgress = true;

        try {
            AgeSignalsManager ageSignalsManager =
                    AgeSignalsManagerFactory.create(context);

            ageSignalsManager
                    .checkAgeSignals(AgeSignalsRequest.builder().build())
                    .addOnSuccessListener(
                            ageSignalsResult -> {
                                Integer lower = ageSignalsResult.ageLower();
                                Integer upper = ageSignalsResult.ageUpper();
                                ageLower = lower == null ? 0 : lower;
                                ageUpper = upper == null ? 150 : upper;
                                valid = true;
                                inProgress = false;
                                Log.i("Age", "Age signals successfully updated.");
                            }
                    )
                    .addOnFailureListener(
                            e -> {
                                valid = false;
                                inProgress = false;
                                Log.e("Age", "Failed to get age signals", e);
                            }
                    );
        } catch (Exception e) {
            inProgress = false;
            Log.e("Age", "Error initiating age signals check", e);
        }
    }
}
