'''
Author Notes:
With this challenge I could understand and learn about smtplib module by creating a smtplib object and sending a message with it. I had to format the text with MIME text method of the
email.mime.text module to be able to use my e-mail server to send the message, since it required the 'From' field correctly filled.
'''
import smtplib
from email.mime.text import MIMEText

def send_email(receiver,subject,message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = 'e-mail'
    msg['To'] = receiver
    print(msg)
    
    user = 'e-mail'
    password ='password'
    server = smtplib.SMTP(host='mail.email.net', port=587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    server.quit()

'''
To execute this code, the code itself needs to be changed. Please, be aware of security concerns and make sure you don't share your password or other relevant data.
user, Password, host (SMTP host), port (SMPT port) and e-mail should be adapted according to your prefered e-mail service.
Once the code is changed, please also adapt and uncomment the line below.
'''

# send_email('receiver','subject','message'):