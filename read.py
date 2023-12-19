
# Importing libraries
import imaplib
import email

imap_url = 'imap.gmail.com'
my_mail = imaplib.IMAP4_SSL(imap_url)
from user_login import *
my_mail.login(my_email, password_key)


my_mail.select("INBOX")


# aaa, data = my_mail.search(None, 'ALL')  
key = 'FROM'
value = 'no-reply@360dialog.com'
aaa, data = my_mail.search(None, key, value)

list = data[0].split()
typ, data = my_mail.fetch(list[0], '(RFC822)')
mail=data[0][1]
msg = email.message_from_bytes(mail)
a=msg['subject']
r=a.encode(encoding = 'utf-8', errors = 'strict')
for i in list:
    typ, data = my_mail.fetch(i, '(RFC822)')
    mail=data[0][1]
    msg = email.message_from_bytes(mail)
    print('Subject:', msg['subject'])
    print('From:', msg['from'])
    print('Data:', msg['Date'])

    for part in msg.walk():  
                #print(part.get_content_type())
                if part.get_content_type() == 'text/plain':
                    print (part.get_payload())
