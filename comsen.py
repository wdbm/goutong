#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# comsen                                                                       #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program composes and sends an e-mail.                                   #
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

name    = "comsen"
version = "2016-03-15T1355Z"

import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():

    print("\ncompose e-mail and send\n")
    message = MIMEMultipart("alternative")
    message["Subject"] = get_input("subject: ")
    message["From"]    = get_input("from (e.g. thecolonel@localhost): ")
    message["To"]      = get_input("to: ")
    text               = get_input("message: ")

    part1 = MIMEText(text, "plain")

    message.attach(part1)

    get_input("\nPress Enter to send.\n")

    try:
        server = smtplib.SMTP("localhost")
        server.sendmail(
            message["From"],
            message["To"],
            message.as_string()
        )
        server.quit()
    except smtplib.SMTPException:
       print("e-mail send error")

def get_input(
    prompt = None
    ):
    if sys.version_info >= (3, 0):
        return input(prompt)
    else:
        return raw_input(prompt)

if __name__ == "__main__":
    main()
