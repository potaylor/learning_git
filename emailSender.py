# LOGIC
# Get email login credentials from service provider
# Using the EmailMessage class from email.message,
#   Build out the email and specify who will be sending and receiving
# Ussing SSL and SMTP
#   Create a default context for SSL
#   Create a SMTP object the uses the created SSL context
#   Use the SMTP to log in to your gmail and send an the EmailMessage object that was created

# CODE
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "princeotaylor@gmail.com"
password = "rrkwjoqejoeuykux"

email_receiver = "pdjohns4@aggies.ncat.edu"

subject = "Python Test"

body = """
Fuck em we ball. All the soldiers we lost
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
