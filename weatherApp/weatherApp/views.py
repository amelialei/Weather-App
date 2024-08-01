from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'index.html')

def get_weather_from_ip(request):
    print(request.GET.get('ip_address'))
    data = {'weather_data': 20}
    return JsonResponse(data)
