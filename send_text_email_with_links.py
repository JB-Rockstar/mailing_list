import smtplib
from email.mime.text import MIMEText

subject = "Artist or Firm Name / Mailing List"
body = "Hello!\n\n" \
       "Thank you for subscribing to my/our mailing list. Here is my Link Tree containing my music and social links: -LINK-.\n\n" \
       "See you soon...\n\n" \
       "-Name-"
sender = "email address of the sender"
to_addr = "email address of the sender (in order for the recipients to be BCC)"
recipients = ["recipient no 1", "recipient no 2", "recipient no 1"]
password = "password (if it is google, write the app password)"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to_addr
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, [to_addr] + recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)
