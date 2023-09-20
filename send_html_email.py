import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

subject = "Welcome to the Mailing List!!!"
body = "Hello!\n\n" \
       "Thank you for subscribing to my/our mailing list.\n\n" \
       "See you soon...\n\n" \
       "-NAME-"
sender = "-Sender email-"
to_addr = "-Sender email-"
mail_list = open('list.txt', 'r').readlines()
recipients = mail_list
password = "-PASSWORD-"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to_addr

    html = open('template.html', 'r').read()

    part1 = MIMEText(body, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    smtp_server = smtplib.SMTP('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, [] + recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)

# JB-ROCKER
# gokhanbalik8@gmail.com
