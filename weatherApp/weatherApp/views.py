from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.conf import settings



def home(request):
    return render(request, 'index.html')

def get_location_from_ip(ip_address):
    response = requests.get('http://ip-api.com/json/{}'.format(ip_address))
    return response.json()

def get_weather_from_location(ip):
    token = settings.WEATHER_TOKEN
    url = f'http://api.weatherapi.com/v1/current.json?key={token}&q={ip}'
    response = requests.get(url)
    return response.json()

def get_weather_from_ip(request):
    ip_address = request.GET.get('ip')
    location = get_location_from_ip(ip_address)
    city = location.get('city')
    weather_data = get_weather_from_location(ip_address)
    temperature = weather_data['current']['temp_f']
    humidity = weather_data['current']['humidity']
    wind = weather_data['current']['wind_mph']
    feels_like = weather_data['current']['feelslike_f']
    pressure = weather_data['current']['pressure_in']
    url = weather_data['current']['condition']['icon']
    # url = "{% static 'images/{}' %}".format(png)
    data = {'Humidity': humidity, 'Wind': wind, 'FeelsLike': feels_like, 'Pressure': pressure, 'Location': city, 'Temperature': temperature, 'WeatherIcon': url}
    return JsonResponse(data)

