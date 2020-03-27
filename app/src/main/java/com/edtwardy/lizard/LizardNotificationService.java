package com.edtwardy.lizard;

import android.util.Log;

import com.google.firebase.messaging.FirebaseMessagingService;

import static android.support.constraint.Constraints.TAG;

public class LizardNotificationService extends FirebaseMessagingService {
    public LizardNotificationService() {
    }

    @Override
    public void onNewToken(String token) {
        Log.d(TAG, "Refreshed Token: " + token);
        sendRegistrationToServer(token);
    }

    private void sendRegistrationToServer(String token) {
        // TODO: Send the registration token to the app server.
    }
}
