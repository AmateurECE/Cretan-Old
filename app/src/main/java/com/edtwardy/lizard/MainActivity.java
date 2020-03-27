package com.edtwardy.lizard;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.google.firebase.iid.FirebaseInstanceId;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Objects;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "Lizard";

    private TextView mTextMessage;
    private String mToken;

    private static final String serverId = "28863855709";

    private Button.OnClickListener mOnClickListener
            = new Button.OnClickListener() {
        @Override
        public void onClick(View v) {
            new Thread(() -> {
                try (Socket socket = new Socket("edtwardy.hopto.org", 13001)) {
                    String message = "REGISTER\n" + mToken + "\n";
                    DataOutputStream out = new DataOutputStream(socket.getOutputStream());
                    out.write(message.getBytes("UTF-8"));
                    DataInputStream in = new DataInputStream(socket.getInputStream());
                    byte [] bytes = new byte[8];
                    if (in.read(bytes, 0, 8) <= 0) {
                        System.err.println("Error while reading server response");
                    }
                    Log.d(TAG, "edtwardy.hopto.org: " + bytes.toString());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }).start();
            mTextMessage.setText("Sent!");
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mTextMessage = findViewById(R.id.message);
        Button button= findViewById(R.id.button);
        button.setOnClickListener(mOnClickListener);

        FirebaseInstanceId.getInstance().getInstanceId()
                .addOnCompleteListener(task -> {
                    if (!task.isSuccessful()) {
                        Log.w(TAG, "getInstanceId failed", task.getException());
                        return;
                    }

                    // Get new Instance ID token
                    mToken = Objects.requireNonNull(task.getResult()).getToken();
                    Log.d(TAG, "Token: " + mToken);
                });


    }

}
