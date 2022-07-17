import requests
import re
from bs4 import BeautifulSoup

def joke():
    r = requests.get('http://piszsuchary.pl/losuj')
    soup = BeautifulSoup(r.text, 'lxml')
    joke = soup.find('pre',class_ = 'tekst-pokaz')
    print(joke.text)

def unusual_holidays():
    r = requests.get('https://www.kalbi.pl/kalendarz-swiat-nietypowych')
    soup = BeautifulSoup(r.text, 'lxml')
    frame = soup.find('div',class_ = 'descritoptions-of-holiday')
    holidays = frame.find_all("a")

    holidays_text = []
    for holiday in holidays:
        holidays_text.append(holiday.text)

    print(holidays_text)

def calendar():
    r = requests.get('https://www.kalbi.pl/')
    soup = BeautifulSoup(r.text, 'lxml')

    frame = soup.find('section', class_ = 'calCard-name-day')
    name_day = frame.find_all('a')
    name_day_text = []
    for name in name_day:
        name_day_text.append(name.text)

    name_day_text = name_day_text[:4]
    print(name_day_text)


    frame = soup.find('div', class_ = 'calCard-astro-sun-hours')
    sun_hours = []
    sunrise = frame.find(text=re.compile('Wsch')).next_sibling.text
    sun_hours.append(sunrise)
    sunset = frame.find(text=re.compile('Zach')).next_sibling.text
    sun_hours.append(sunset)

    print(sun_hours)

if __name__ == "__main__":
    joke()
    unusual_holidays()
    calendar()