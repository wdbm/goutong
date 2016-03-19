#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# rec                                                                          #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program receives e-mail.                                                #
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

name    = "rec"
version = "2016-03-19T2051Z"

import asyncore
import shijian
from smtpd import SMTPServer

def main():
    server = Server(("localhost", 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass

class Server(SMTPServer):
    def process_message(
        self,
        peer,
        mailfrom,
        rcpttos,
        data
    ):
        filename = "{timestamp}.eml".format(timestamp = shijian.time_UTC())
        file_email = open(filename, "w")
        print("save file {filename}".format(filename = filename))
        file_email.write(data)
        file_email.close

if __name__ == '__main__':
    main()
