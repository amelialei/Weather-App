from django.shortcuts import render
from django.http import JsonResponse
import requests

def home(request):
    return render(request, 'index.html')

def get_location_from_ip(ip_address):
    response = requests.get('http://ip-api.com/json/{}'.format(ip_address))
    return response.json()

def get_weather_from_location(city, country_code):
    token = '75e9e26e48979768aa2f20f0dfbd2f41'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid={}'.format(
        city, country_code,token)
    response = requests.get(url)
    return response.json()

def get_weather_from_ip(request):
    ip_address = request.GET.get('ip')
    location = get_location_from_ip(ip_address)
    city = location.get('city')
    country_code = location.get('countryCode')
    weather_data = get_weather_from_location(city, country_code)
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind = weather_data['wind']['speed']
    feels_like = weather_data['main']['feels_like']
    pressure = weather_data['main']['pressure']
    data = {'Humidity': humidity, 'Wind': wind, 'FeelsLike': feels_like, 'Pressure': pressure, 'Location': city, 'Temperature': temperature}
    return JsonResponse(data)
