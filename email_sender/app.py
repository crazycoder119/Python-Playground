# go over to our gmail account and setup 2 factor authentication
# generate app password
# create function to send the mail


from email.message import  EmailMessage
from passwordManager import app_pass
import ssl
import smtplib

email_sender = 'eagleaidev@gmail.com'
email_password = app_pass

email_receiver = 'dafiyi8667@dineroa.com'

subject = "Hey its playtime"
body = """
    Hey whats on the schedule :)
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

