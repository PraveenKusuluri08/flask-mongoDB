import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


class Email:
    sender_email = "noreplytoapp@gmail.com"
    password = os.getenv("SMTP_PASSWORD")
    def __init__(self):
        pass
    
    @staticmethod
    def send_email_to_user(to, subject, html):
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = Email.sender_email
        message["To"] = to
        part = MIMEText(html, "html")
        message.attach(part)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(Email.sender_email, Email.password)

            server.sendmail(
                Email.sender_email, to, message.as_string()
            )
