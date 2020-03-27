///////////////////////////////////////////////////////////////////////////////
// NAME:            iServer.h
//
// AUTHOR:          Ethan D. Twardy <edtwardy@mtu.edu>
//
// DESCRIPTION:     Server interface
//
// CREATED:         03/27/2020
//
// LAST EDITED:     03/27/2020
////

#ifndef __ET_ISERVER__
#define __ET_ISERVER__

#include <namespaces/Interfaces.h>

class Cretan::Interfaces::iServer
{
public:
  virtual void runLoop() = 0;
};

#endif // __ET_ISERVER__

///////////////////////////////////////////////////////////////////////////////
