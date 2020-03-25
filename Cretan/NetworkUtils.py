###############################################################################
# NAME:             NetworkUtils.py
#
# AUTHOR:           Ethan D. Twardy <edtwardy@mtu.edu>
#
# DESCRIPTION:      Contains some useful classes for writing networked stuff.
#
# CREATED:          12/12/2019
#
# LAST EDITED:      03/24/2020
###

from socket import socket, AF_INET, SOCK_STREAM
import contextlib
import traceback

###############################################################################
# Class Server
###

class Server:
    """Implements a Generic networked Server
    How to use:
        1 Write a class Session, which handles a connection from a client.
          Session must have a .handle() method taking no arguments and return
          immediately after the session is complete.
        2 Write a SessionFactory class, which has a .make() method, taking the
          socket for the connection and the address of the incoming connection.
          Must return a Session instance.
        3 Instantiate a Server, then invoke .run().
    """
    def __init__(self, portNumber, sessionFactory, logfn=print):
        self.serverSocket = None
        self.portNumber = portNumber
        self.sessionFactory = sessionFactory
        self.logfn = logfn

    def __enter__(self):
        """Enter a context"""
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        # TODO: What happens if we don't get our port number?
        self.serverSocket.bind(('', self.portNumber))
        self.portNumber = self.serverSocket.getsockname()[1]
        return self

    def __exit__(self, exceptType, exceptValue, traceBack):
        """Exit a context"""
        if exceptType is None:
            self.serverSocket.close()
        else:
            traceback.print_exception(exceptType, exceptValue, traceBack)
        return self

    def run(self):
        """Be open to receiving connections and stuff"""
        self.serverSocket.listen(1024)
        self.logfn('Server: Listening on port {}...'.format(self.portNumber))

        while True:
            with Server.acceptClient(self.serverSocket) \
                 as (clientSock, address):
                self.logfn(('Server: Connection from addresss {},\n'
                            '        Handling on {}'
                           .format(address, clientSock.getsockname())))
                session = self.sessionFactory.make(clientSock, address,
                                                   logfn=self.logfn)
                session.handle()

    @staticmethod
    @contextlib.contextmanager
    def acceptClient(sock):
        """Context Manager for the socket class."""
        clientSock, address = sock.accept()
        yield clientSock, address
        clientSock.close()

###############################################################################
# Client
###

class Client:
    """Implements the logic of a Generic Client
    How to use: Create a Client object using a with..as block. Interact with
    the server by sending plaintext messages usin the .sendMessage() method.
    """
    def __init__(self, server, port):
        self.serverName = server
        self.serverPort = port
        self.clientSock = None

    def __enter__(self):
        """Set up the connection"""
        self.clientSock = socket(AF_INET, SOCK_STREAM)
        self.clientSock.connect((self.serverName, self.serverPort))
        return self

    def __exit__(self, exceptType, exceptValue, traceBack):
        """Exit a context"""
        if exceptType is None:
            self.clientSock.close()
        else:
            traceback.print_exception(exceptType, exceptValue, traceBack)
        return self

    def sendMessage(self, message):
        """Sends a message to the server."""
        self.clientSock.send(message.encode())
        return self.clientSock.recv(2048).decode()

###############################################################################
# Main
###

def main():
    """Empty main method"""
    return 0

# Only for formality
if __name__ == '__main__':
    main()

###############################################################################
