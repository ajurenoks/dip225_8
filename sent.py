import smtplib 
import email
from email.message import EmailMessage
from user_login import *

# SMTP Server and port no for GMAIL.com
gmail_server= "smtp.gmail.com"
gmail_port= 587


# Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()
    
# Login with your email and password
my_server.login(my_email, password_key)
msg = EmailMessage()
msg.set_content('This is my message')

msg['Subject'] = 'Testa mail'
msg['From'] = "aleksejs.jurenoks@gmail.com"
msg['To'] = "aleksejs.jurenoks@gmail.com"

my_server.send_message(msg)
print('Mail Sent')