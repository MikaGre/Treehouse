import requests


from tests.utils.keys import api_key


def reqbycityname(city_name):
    return requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')


def reqbyzipcode(zip_code, country_code):
    return requests.get(f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={api_key}')
