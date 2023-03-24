import requests
import json
import csv

from tests.utils.keys import api_key


city = 'New York'
country = 'US'
units = 'imperial'


res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units={units}&appid={api_key}')
data = res.json()
#print(json.dumps(res.json(), indent=4))
#print(json.dumps(res['weather'][0]['description'], indent=4))

weather = data['weather'][0]['main']
temp = data['main']['temp']
wind_speed = data['wind']['speed']


header = ['city', 'country_code', 'weather', 'temp', 'wind_speed']
info = [city, country, weather, temp, wind_speed]

with open('weather.csv', 'w') as f:
        writer = csv.writer(f)
        #write header
        writer.writerow(header)
        #write data
        writer.writerow(info)