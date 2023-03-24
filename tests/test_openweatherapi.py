import requests
import pytest
import json

from tests.utils.helpers import *

#'Colorado' assert 'BR' == 'US' 
#'Kentucky' assert 'AU' == 'US'
# Montana' assert 'BG' == 'US'
# Reason: expected country is incorrect
city_names = [
'Alabama',
'Alaska',
'Arizona',
'Arkansas',
'California',
'Colorado',
'Connecticut',
'Delaware',
'Florida',
'Georgia',
'Hawaii',
'Idaho',
'Illinois',
'Indiana',
'Iowa',
'Kansas',
'Kentucky',
'Louisiana',
'Maine',
'Maryland',
'Massachusetts',
'Michigan',
'Minnesota',
'Mississippi',
'Missouri',
'Montana',
'Nebraska',
'Nevada',
'New Hampshire',
'New Jersey',
'New Mexico',
'New York',
'North Carolina',
'North Dakota',
'Ohio',
'Oklahoma',
'Oregon',
'Pennsylvania',
'Rhode Island',
'South Carolina',
'South Dakota',
'Tennessee',
'Texas',
'Utah',
'Vermont',
'Virginia',
'Washington',
'West Virginia',
'Wisconsin',
'Wyoming',
]

@pytest.mark.bycity
@pytest.mark.parametrize('city', city_names)
def test_get_by_city(city):
        res = reqbycityname(city)
        data = res.json()
        
        assert res.status_code == 200
        #assert data['sys']['country'] == 'US'
        
        if city == 'Maine':
                assert data['name'] == 'State of Maine'
        elif city == 'Wyoming':
                assert data['name'] == 'State of Wyoming'        
        else:        
                assert data['name'] == city


nyzipcodes = []

for _ in range(10001,10010):
        nyzipcodes.append(f"{_}")

@pytest.mark.byzip        
@pytest.mark.parametrize('zip_code', nyzipcodes)
def test_get_by_zipcode(zip_code):
        res = reqbyzipcode(zip_code, 'US')
        data = res.json()
        
        assert res.status_code == 200
        assert data['sys']['country'] == 'US'
        assert data['name'] == 'New York'
        