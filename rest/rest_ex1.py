# A sample script for begining REST API and Python

import requests
import json
from pprint import pprint


def openweather(city):
    openweather_url = 'http://api.openweathermap.org/data/2.5/weather'
    city_prefix = '?q='
    token_prefix = '&appid='
    token = '22daa42db2ba52ddead5e20bddc59af1'
    unit_prefix = '&units='
    unit = 'metric'

    url_api = openweather_url + city_prefix + city + token_prefix + \
              token + unit_prefix + unit

    temp = requests.get(url_api).json()

    return temp


def main():
    # city = input('Enter City: ')
    cities = ['Sydney', 'Cairo', 'Moscow', 'New York', 'Gilbert']
    for city in cities:
       # Send city to openweather function
        temp = openweather(city)
        city_temp = temp['main']['temp']
        city_condition = temp['weather'][0]['description']
        print('City: ' + city, 'temp ', city_temp, 'condition ', city_condition)


if __name__ == '__main__':
    main()