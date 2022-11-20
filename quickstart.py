from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def get_calendar():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # Notice Solari: for automatic tasks, use the absolute path, e.g. /home/jjbg/solari_scripts/dzien_dobry/token.json
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
    # Notice Solari: for automatic tasks, use the absolute path, e.g. /home/jjbg/solari_scripts/dzien_dobry/credentials.json
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        to = (datetime.datetime.utcnow()  + datetime.timedelta(days=3)).isoformat() + 'Z'  # 'Z' indicates UTC time

        calendars = [('Bartek','primary'),('Ania','liliana89ana@gmail.com'),('RDabrowa','rachunkidabrowa@gmail.com')]
        calendars_text = ''

        for calendar in calendars:
            calendars_text = calendars_text + calendar[0] + '<br>'
            events_result = service.events().list(calendarId=calendar[1], timeMin=now, timeMax=to, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                calendars_text = calendars_text + 'Cisza na horyzoncie.<br><br>'

            # Prints the start and name of the next 10 events
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                calendars_text = calendars_text + start + ' ' + event['summary'] + '<br>'

                if event == events[-1]:
                    calendars_text = calendars_text + '<br>'

        return calendars_text

    except HttpError as error:
        print('An error occurred: %s' % error)