import google.auth.exceptions
import requests
import datetime
import logging
import quickstart
from bs4 import BeautifulSoup
import cloudscraper
from v_email import send_mail

# logging start app, end app, errors
logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)



def joke():
    """
    Get joke from kinyen.pl
    :return: str
    """
    try:
        r = requests.get('http://kinyen.pl/dowcipy/losowy/')
        soup = BeautifulSoup(r.text, 'lxml')
        joke = soup.find('div', class_='joke').get_text(strip=True)

        return joke

    except Exception as e:
        logging.exception('Joke function problem')


def garfield():
    """
    Get random comic of garfield from https://www.gocomics.com/random/garfield
    :return: str
    """
    try:
        url = 'https://www.gocomics.com/garfield'
        scraper = cloudscraper.create_scraper()
        html = scraper.get(url).text
        soup = BeautifulSoup(html, 'lxml')

        img = soup.find("img", class_=lambda c: c and "Comic_comic__image__" in c)

        return img["src"]
    except Exception as e:
        logging.exception('Mem function problem')

def bible():
    """
    Get random werset from Bible
    :return: str
    """
    try:
        r = requests.get('https://dailyverses.net/pl/losowy-werset-biblii/bw1975')
        soup = BeautifulSoup(r.text, 'lxml')
        word = soup.find('span', class_='v1').get_text()
        word = word + '-' + soup.find('a', class_='vc').get_text()

        return word
    except Exception as e:
        logging.exception('Bible function problem')


def wiselka():
    """
    Get next matches of Wisla Krakow from wislaportal.pl
    :return: str
    """
    try:
        r = requests.get('https://www.wislaportal.pl', verify=False)

        #polish chars
        r.encoding = "utf-8"

        soup = BeautifulSoup(r.text, 'lxml')
        frame = soup.find('div', class_='match-card-modern next-match')

        date = frame.find('i', class_='fa fa-calendar-o').next_element.get_text()

        teams_row = frame.find_all('div', recursive=False)[1]
        cols = teams_row.find_all('div', recursive=False)
        home_team = cols[0].get_text(strip=True)
        away_team = cols[2].get_text(strip=True)

        matches_text = date + home_team + "-" + away_team


        return matches_text
    except Exception as e:
        logging.exception('Wiselka function problem')


def unusual_holidays():
    """
    Get unsusual holidays
    :return: str
    """
    try:
        r = requests.get('https://www.kalbi.pl/kalendarz-swiat-nietypowych')
        soup = BeautifulSoup(r.text, 'lxml')
        holidays = soup.find('div', class_='descritoptions-of-holiday').find_all("h3")

        holidays_text = ''
        for holiday in holidays:
            holidays_text = holidays_text + str(holiday.text) + '<p>'

        return holidays_text
    except Exception as e:
        logging.exception('Unusual function mode function problem')


def weather():
    """
    Get weather by API open-meteo.com
    Docs: https://open-meteo.com/en/docs
    :return: str
    """
    try:
        r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.392051&longitude=16.790847&&timezone=auto&daily=temperature_2m_max&daily=temperature_2m_min&daily=sunrise&daily=sunset&daily=sunrise&daily=precipitation_sum&daily=weathercode').json()
        temp_max = r['daily']['temperature_2m_max'][0]
        temp_min = r['daily']['temperature_2m_min'][0]
        sunrise = r['daily']['sunrise'][0][-5:]
        sunset = r['daily']['sunset'][0][-5:]

        return temp_max, temp_min, sunrise, sunset
    except Exception as e:
        logging.exception('Weather function problem')


def name_day():
    """
    Get nameday - first 3.
    :return: str
    """
    try:
        r = requests.get('https://www.kalbi.pl/')
        soup = BeautifulSoup(r.text, 'lxml')

        name_day = soup.find('section', class_='calCard-name-day').find_all('a')
        name_day_text = ''
        for name in name_day[:3]:
            name_day_text = name_day_text + name.text + ', '

        name_day_text = name_day_text[:-2]

        return name_day_text
    except Exception as e:
        logging.exception('Name day function problem')

def date_today():
    """
    Get name of day and date
    :return: str
    """
    try:
        days = {"0": "niedzielę", "1": "poniedziałek", "2": "wtorek", "3": "środę", "4": "czwartek", "5": "piątek", "6": "sobotę"}
        number = datetime.datetime.today().strftime("%w")
        day_of_week = days[number]
        pl_date = datetime.datetime.today().strftime("%d" "." "%m" "." "%y")

        return day_of_week, pl_date
    except Exception as e:
        logging.exception('Date today function problem')


if __name__ == "__main__":
    """
    Main function. Call next fuctions, assign to the variables and send mail (html content).
    """
    try:
        logging.info('Run script')

        name_day = name_day()
        joke = joke()
        unusual_holidays = unusual_holidays()
        temp_max, temp_min, sunrise, sunset = weather()
        matches = wiselka()
        word = bible()
        day_of_week, pl_date = date_today()
        garfield = garfield()

        # direct from tutorial Google - https://developers.google.com/calendar/api/quickstart/python
        events_calendar = quickstart.get_calendar()

        send_mail(day_of_week, pl_date, name_day, temp_max, temp_min, sunrise, sunset, unusual_holidays, joke, matches, word, events_calendar,garfield)
        logging.info('Done')

    except google.auth.exceptions.RefreshError as re:
        logging.exception('Wygasl token API Google Calendar')

    except Exception as e:
        logging.exception('Main function problem')
