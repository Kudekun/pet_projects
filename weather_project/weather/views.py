from django.shortcuts import render
import requests
from django.conf import settings

def index(request):
    weather_data = None
    city = None
    map_url = None
    error_message = None

    if 'city' in request.GET:
        city = request.GET['city']
        api_key = settings.WEATHER_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            lat = weather_data['coord']['lat']
            lon = weather_data['coord']['lon']
            map_url = f'https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d41556.58856035984!2d{lon}!3d{lat}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1suk!2sua!4v1723832668322!5m2!1suk!2sua'
        else:
            error_message = 'Місто не знайдено.'

    return render(request, 'index.html', {'weather': weather_data, 'city': city, 'map_url': map_url, 'error_message': error_message})