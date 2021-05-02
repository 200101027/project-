import requests
import json


BASE_URL = 'https://api.covid19api.com'
COUNTRY_STATISTICS_URL = BASE_URL + '/country/{country}'



def get_country_statistics(country='kazakhstan'):
    data = requests.get(COUNTRY_STATISTICS_URL.format(country=country)).text
    res = json.loads(data)
    return res


def get_last_statistics(country='kazakhstan'):
    data = get_country_statistics(country)
    return data[-1]

