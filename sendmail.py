import requests
import wget
import smtplib, ssl, email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    print('Connection OK..')
except:
    print('Connection Disconnected...')


port = 587
smtp_server = "smtp.gmail.com"
sender_mail = "haerul.pda@gmail.com"
receiver_mail = "dummytgr2@gmail.com"
password = input("Enter email password : ")

subject = 'Tes email with attachment'
body = 'ini test email '
massage = MIMEMultipart()
massage['FROM'] = sender_mail
massage['TO'] = receiver_mail
massage['Subject'] = subject

massage.attach(MIMEText(body, "PLAIN"))
filename = 'tes.pdf'

with open(filename, 'rb') as attachment:
    part = MIMEBase("")
# massage = """\
# Subject: Hi there
#
# This massage send from python."""

context  = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_mail, password)
    server.sendmail(sender_mail, receiver_mail, massage)
