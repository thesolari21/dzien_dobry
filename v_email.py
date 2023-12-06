import smtplib, ssl,logging
from email.message import EmailMessage
import html_template as ht
import json

def send_mail(day_of_week, pl_date, name_day, temp_max, temp_min, sunrise, sunset, unusual_holidays, joke, matches, word, events_calendar,garfield):
    """
    send mail html injecting the received variables into the template.
    Template in html_template file.
    :return: None
    """

    with open('config.json','r') as f:
        config = json.load(f)

    try:
        port = config['port']  # For SSL
        smtp_server = config['smtp_server']
        sender_email = config['sender_email']
        receiver_email = config['receiver_email']
        password = config['password']

        #need to be devided, problem with read css tags when injects python variables
        header_html = ht.header
        body_html = ht.body.format(day_of_week=day_of_week, pl_date=pl_date, name_day=name_day, temp_max=temp_max, temp_min=temp_min, sunrise=sunrise, sunset=sunset, unusual_holidays=unusual_holidays, joke=joke, matches=matches, word=word, events_calendar = events_calendar, garfield = garfield)
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