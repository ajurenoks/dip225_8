
# Importing libraries
import imaplib
import email

imap_url = 'imap.gmail.com'
my_mail = imaplib.IMAP4_SSL(imap_url)
from user_login import *
my_mail.login(my_email, password_key)

box=[]
for i in my_mail.list()[1]:
    l = i.decode().split(' "/" ')
    box.append(l[1])


my_mail.select(box[12])


# aaa, data = my_mail.search(None, 'ALL')  
key = 'FROM'
value = 'noreply@macam.lv'
aaa, data = my_mail.search(None, key, value)

list = data[0].split()

for i in list:
    # my_mail.store(i,'+X-GM-LABELS', '\\Trash')
    my_mail.store(i, '+FLAGS', '\\Deleted')

my_mail.expunge()
my_mail.close()
my_mail.logout()
