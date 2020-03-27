///////////////////////////////////////////////////////////////////////////////
// NAME:            TCPServer.h
//
// AUTHOR:          Ethan D. Twardy <edtwardy@mtu.edu>
//
// DESCRIPTION:     A class that listens for TCP connections.
//
// CREATED:         03/27/2020
//
// LAST EDITED:     03/27/2020
////

#ifndef __ET_TCPSERVER__
#define __ET_TCPSERVER__

#include <Interfaces/iServer.h>

#include <namespaces/Networking.h>

class Cretan::Networking::TCPServer : Cretan::Interfaces::iServer
{
public:
  using Handler = std::function<void(Cretan::Networking::ConnectedSocket&&)>;
  TCPServer(Handler connectionHandler);

  virtual void runLoop() final override;
private:
  Handler connectionHandler;
};

#endif // __ET_TCPSERVER__

///////////////////////////////////////////////////////////////////////////////
