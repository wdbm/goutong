# goutong

## introduction

The User Datagram Protocol (UDP) is one of the core members of the Internet protocol suite. The protocol was designed by David P. Reed in 1980 and defined in [RFC 768](https://www.ietf.org/rfc/rfc768.txt).

Currently, goutong is a basic UDP communications program implemented in Python using sockets. It can operate in point-to-point mode or broadcast mode. Broadcast mode is engaged by setting the last byte of the I.P. address to 255, for example 192.168.0.255.  The default port is 2718. A list of Transmission Control Protocol (TCP) and UDP port numbers is [here](http://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers).

## quick start point-to-point

To start point-to-point communications between two nodes, run an instance of goutong on each node. For each instance, set the I.P. address of the other node, in a way such as the following:

- node 1:
    - I.P. address: 188.184.68.240
    - port: 2718
- node 2:
    - I.P. address: 188.184.68.250
    - port: 2718

Point-to-point communications should be available now.

# future

Under consideration is making goutong more modular and functional, for the purposes of program internal communications.
