import smtplib
import asyncio
import logging
import aiofiles
import aiosmtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

async def send_validation_url(url_to_send, receiver_address):
    def _send_validation_url_sync(url_to_send, receiver_address):
        html_location = os.getenv("HTML_LOCATION")

        with open(html_location + "validation_mail.html", mode="r") as f:
            html = f.read()
            mail_content = html.replace("[URL]", url_to_send)

        sender_address = 'r.mejri74100@gmail.com'
        sender_pass = os.environ.get("GMAIL_PASSWORD")

        if sender_pass is None:
            raise Exception("Missing GMAIL_PASSWORD environnement variable to send mail")
            
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "Validation d'inscription à l'application EatWas"
        message.attach(MIMEText(mail_content, 'html'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

    
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, _send_validation_url_sync, url_to_send, receiver_address)
    
async def send_reset_password_link(url_to_send, receiver_address):
    def _send_reset_password_sync(url_to_send, receiver_address):
        sender_address = 'r.mejri74100@gmail.com'
        sender_pass = os.environ.get("GMAIL_PASSWORD")

        if sender_pass is None:
            raise Exception("Missing GMAIL_PASSWORD environnement variable to send mail")
            
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = "Demande réinitialisation de mot de passe à l'application EatWas"
        message.attach(MIMEText(url_to_send, 'html'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, _send_reset_password_sync, url_to_send, receiver_address)