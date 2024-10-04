import requests
from django.conf import settings

class OpenWeatherMapClient:
    def __init__(self):
        self.api_key = settings.WEATHER_API_KEY
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'uk'
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

