#!/usr/bin/env python
import socket
import sys
import select

def main():

    defaultPortNumber   = 2718
    host                = raw_input("Enter I.P. address: ")
    portNumber          = raw_input(
        "Enter port number (default {defaultPortNumber}): ".format(
            defaultPortNumber = defaultPortNumber
        )
    ) or defaultPortNumber
    port                = int(str(portNumber), 10)
    addressRemote       = (host, port)
    # Create a datagram socket for UDP.
    socketUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set the socket to be reusable.
    socketUDP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Set the socket to accept incoming broadcasts.
    socketUDP.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Disengage socket blocking.
    socketUDP.setblocking(False)
    # Set the socket to accept connections on the port.
    socketUDP.bind(('', port))
    print("accept connections on port {portNumber}".format(
        portNumber = str(hex(port))
    ))
    # Communicate data in a loop.
    while True:
        # receive
        try:
            # buffer size: 8192 (change as needed)
            message, address = socketUDP.recvfrom(8192)
            if message:
                print("{address}:{portNumber}> {message}".format(
                    address    = address[0],
                    portNumber = portNumber,
                    message    = message.rstrip('\n')
                ))
        except:
            pass
        # send
        inputMessage = getLine();
        if inputMessage != False:
            socketUDP.sendto(inputMessage, addressRemote)

# Read a line. Using select for non-blocking reading of sys.stdin.
def getLine():

    i, o, e = select.select([sys.stdin], [], [], 0.0001)
    for s in i:
        if s == sys.stdin:
            inputMessage = sys.stdin.readline()
            return(inputMessage)
    return(False)

if __name__ == '__main__':
    main()
