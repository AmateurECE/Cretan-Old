###############################################################################
# NAME:             SendMessage.py
#
# AUTHOR:           Ethan D. Twardy <edtwardy@mtu.edu>
#
# DESCRIPTION:      Connects to the CretanServer and sends a message to a
#                   device.
#
# CREATED:          03/24/2020
#
# LAST EDITED:      03/25/2020
###

import argparse
from NetworkUtils import Client

###############################################################################
# Main
###

def parseArguments():
    """Parse arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("device", help=('The Device ID of the recipient'))
    parser.add_argument("message", help=('The content of the message'))
    return parser.parse_args()

def main():
    args = parseArguments()
    with Client('192.168.1.60', 13001) as client:
        message = ('SEND_MESSAGE\n'
                   + args.device + '\n'
                   + args.message + '\n')
        response = client.sendMessage(message)
        if response == 'OK':
            print('Sent successfully')
        else:
            print('Error while sending message! Got: "{}"'.format(response))

if __name__ == '__main__':
    main()

###############################################################################
