#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# e-mail_1                                                                     #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program sends an e-mail.                                                #
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

name    = "e-mail_1"
version = "2016-03-15T1401Z"

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main():

    message = MIMEMultipart("alternative")
    message["Subject"] = "We are watching you."
    message["From"]    = "thecolonel@localhost"
    message["To"]      = "mulder@fbi.g0v"
    
    text = "The Event is at hand."
    html = """\
    <html>
    <head></head>
    <body>
    <p>
    The Event is at hand.
    </p>
    </body>
    </html>
    """
    
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    message.attach(part1)
    message.attach(part2)
    
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

if __name__ == "__main__":
    main()
