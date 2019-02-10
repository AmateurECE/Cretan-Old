#!/usr/bin/env python3
###############################################################################
# NAME:             DownstreamMessaging.py
#
# AUTHOR:           Ethan D. Twardy <edtwardy@mtu.edu>
#
# DESCRIPTION:      This module contains a simplified API for sending
#                   downstream messages to Android devices.
#
# CREATED:          01/25/2019
#
# LAST EDITED:      02/09/2019
###

###############################################################################
# IMPORTS
###

from firebase_admin import messaging

###############################################################################
# CLASSES
###

class Messenger():
    """Object that communicates with the FCM server on behalf of the app."""
    def __init__(self, registrationToken):
        self.registrationToken = registrationToken

    def sendMessage(self, title, body):
        """
        Send a message to the device that this Messenger is paired with.
        """
        message = messaging.Message(
            data={
                "title": title,
                "body": body
            },
            token=self.registrationToken
        )
        return messaging.send(message)

    @staticmethod
    def exampleMessage():
        """Gives an example for message sending."""
        # This example message only works if device.token is a file in the
        # current directory.
        with open('device.token', 'r') as tokenFile:
            # Read in the registration token. Readline() does not chomp the
            # terminating newline, hence the slice.
            registrationToken = tokenFile.readline()[:-1]
            message = messaging.Message(
                data={
                    "title": "Lizard-Server",
                    "body": "Ethan D. Twardy"
                },
                token=registrationToken,
            )
            return messaging.send(message)

###############################################################################
# MAIN
###

if __name__ == '__main__':
    print('DownstreamMessaging.py')

##############################################################################
