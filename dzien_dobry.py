import requests
import re
import datetime
import logging
from bs4 import BeautifulSoup
from v_email import send_mail

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

def joke():
    try:
        r = requests.get('http://piszsuchary.pl/losuj')
        soup = BeautifulSoup(r.text, 'lxml')
        joke = soup.find('pre', class_='tekst-pokaz')
        joke_text = joke.text
        joke_text = joke_text[:-16]

        return joke_text
    except Exception as e:
        logging.exception('Joke function problem')


def english_word():
    try:
        r = requests.get('https://www.diki.pl/dictionary/word-of-the-day')
        soup = BeautifulSoup(r.text, 'lxml')
        word = soup.find('div', class_='dictionaryEntity').find_all('a', class_='plainLink')
        word = word[0].text + ' - ' + word[1].text
        example_sentence = soup.find('div', class_='exampleSentence').text.strip().replace('   ', '')

        word = word + '<br><br>' + example_sentence

        return word
    except Exception as e:
        logging.exception('English word function problem')


def wiselka():
    try:
        r = requests.get('https://www.wislaportal.pl')
        r.encoding = "iso-8859-2"
        soup = BeautifulSoup(r.text, 'lxml')
        frame = soup.find(text=re.compile('NAJBLIŻSZE')).next_element.next_element
        matches = frame.find_all('li')

        matches_text = ''
        for match in matches:
            temp = match.text.replace("\n", "").replace(" ", "   ") + "<p>"
            matches_text = matches_text + temp

        return matches_text
    except Exception as e:
        logging.exception('Wiselka function problem')


def unusual_holidays():
    try:
        r = requests.get('https://www.kalbi.pl/kalendarz-swiat-nietypowych')
        soup = BeautifulSoup(r.text, 'lxml')
        holidays = soup.find('div', class_='descritoptions-of-holiday').find_all("h3")

        holidays_text = ''
        for holiday in holidays:
            holidays_text = holidays_text + str(holiday.text) + '<br>'

        return holidays_text
    except Exception as e:
        logging.exception('Unusual function mode function problem')


def weather():
    try:
        r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.392051&longitude=16.790847&&timezone=auto&daily=temperature_2m_max&daily=temperature_2m_min&daily=sunrise&daily=sunset&daily=sunrise&daily=precipitation_sum&daily=weathercode').json()
        temp_max = r['daily']['temperature_2m_max'][0]
        temp_min = r['daily']['temperature_2m_min'][0]
        sunrise = r['daily']['sunrise'][0][-5:]
        sunset = r['daily']['sunset'][0][-5:]

        return temp_max, temp_min, sunrise, sunset
    except Exception as e:
        logging.exception('Weather function problem')


def weather_icon():
    try:
        r = requests.get('https://pogoda.onet.pl/prognoza-pogody/dabrowa-281445')
        soup = BeautifulSoup(r.text, 'lxml')
        src = soup.find('div', class_='forecast').find('img')

        return 'https:'+src['src']
    except Exception as e:
        logging.exception('Weather icon function problem')

def name_day():
    try:
        r = requests.get('https://www.kalbi.pl/')
        soup = BeautifulSoup(r.text, 'lxml')

        name_day = soup.find('section', class_='calCard-name-day').find_all('a')
        name_day_text = ''
        for name in name_day[:5]:
            name_day_text = name_day_text + name.text + ', '

        name_day_text = name_day_text[:-2]

        return name_day_text
    except Exception as e:
        logging.exception('Name day function problem')

def date_today():
    try:
        days = {"0": "niedzielę", "1": "poniedziałek", "2": "wtorek", "3": "środę", "4": "czwartek", "5": "piątek", "6": "sobotę"}
        number = datetime.datetime.today().strftime("%w")
        day_of_week = days[number]
        pl_date = datetime.datetime.today().strftime("%d" "." "%m" "." "%y")

        return day_of_week, pl_date
    except Exception as e:
        logging.exception('Date today function problem')


if __name__ == "__main__":
    try:
        logging.info('Run script')

        name_day = name_day()
        joke = joke()
        unusual_holidays = unusual_holidays()
        temp_max, temp_min, sunrise, sunset = weather()
        matches = wiselka()
        word = english_word()
        day_of_week, pl_date = date_today()
        src_icon = weather_icon()

        send_mail(day_of_week, pl_date, name_day, src_icon, temp_max, temp_min, sunrise, sunset, unusual_holidays, joke, matches, word)
        logging.info('Done')
    except Exception as e:
        logging.exception('Main function problem')
