#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# goutong                                                                      #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a point-to-point UDP communications program.                 #
#                                                                              #
# copyright (C) 2016 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

name    = "goutong"
version = "2016-03-15T1356Z"

import socket
import sys
import select

def main():

    port_number_default = 2718
    host                = get_input("Enter I.P. address: ")
    port_number         = get_input(
        "Enter port number (default {port_number_default}): ".format(
            port_number_default = port_number_default
        )
    ) or port_number_default
    port                = int(str(port_number), 10)
    address_remote      = (host, port)
    # Create a datagram socket for UDP.
    socket_UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set the socket to be reusable.
    socket_UDP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Set the socket to accept incoming broadcasts.
    socket_UDP.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Disengage socket blocking.
    socket_UDP.setblocking(False)
    # Set the socket to accept connections on the port.
    socket_UDP.bind(('', port))
    print("accept connections on port {port_number}".format(
        port_number = str(hex(port))
    ))
    # Communicate data in a loop.
    while True:
        # receive
        try:
            # buffer size: 8192 (change as needed)
            message, address = socket_UDP.recvfrom(8192)
            if message:
                print("{address}:{port_number}> {message}".format(
                    address     = address[0],
                    port_number = port_number,
                    message     = message.rstrip('\n')
                ))
        except:
            pass
        # send
        input_message = get_line();
        if input_message != False:
            socket_UDP.sendto(input_message, address_remote)

def get_input(
    prompt = None
    ):
    if sys.version_info >= (3, 0):
        return input(prompt)
    else:
        return raw_input(prompt)

# Read a line using select for non-blocking reading of sys.stdin.
def get_line():
    i, o, e = select.select([sys.stdin], [], [], 0.0001)
    for s in i:
        if s == sys.stdin:
            input_message = sys.stdin.readline()
            return(input_message)
    return(False)

if __name__ == '__main__':
    main()
