#import requirements modules
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



#server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "koushikadineni@gmail.com"
passkey = "yustolqukfyclnvj"

def singleEmailsend(to_email:str, subject:str,body:str):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))


    try:
        #start server
        server = SMTP(smtp_server, smtp_port)
        #start server
        server.starttls()
        #log in to server
        server.login(sender_email, passkey)
        #sender email
        server.sendmail(from_addr=sender_email,
                        to_addrs=to_email,
                        msg=msg.as_string())
        server.quit()
        return f"Successfully email send to {to_email}"
    except Exception as e:
        return f"Failed to send email because:{e}"
    

to_email = input("Enter Email address:")
subject = input("Enter email Subject:")
body = input("Enter email body:")
#call singleemail send
print(singleEmailsend(to_email, subject, body))
