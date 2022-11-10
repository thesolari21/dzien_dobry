import smtplib, ssl,logging
from email.message import EmailMessage
import html_template as ht

def send_mail(day_of_week, pl_date, name_day, src_icon, temp_max, temp_min, sunrise, sunset, unusual_holidays, joke, matches, word):
    try:
        port = 465  # For SSL
        smtp_server = ""    # Enter smtp server
        sender_email = ""   # Enter sender email
        receiver_email = "" # Enter receiver mail
        password = ""       # Enter password smtp server

        #need to be devided, problem with read css tags when injects python variables
        header_html = ht.header
        body_html = ht.body.format(day_of_week=day_of_week, pl_date=pl_date, name_day=name_day, src_icon=src_icon, temp_max=temp_max, temp_min=temp_min, sunrise=sunrise, sunset=sunset, unusual_holidays=unusual_holidays, joke=joke, matches=matches, word=word)
        content = header_html + body_html

        msg = EmailMessage()
        msg['Subject'] = 'Miłego dnia!'
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(content, subtype='html')

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)
    except Exception as e:
        logging.exception('Mail function problem')
        print(e)