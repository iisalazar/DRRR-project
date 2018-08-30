from django.shortcuts import render
import requests

# Create your views here.

api_key = '5ed50787e4f36a97057b04bdf51623f1'

def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
    r = requests.get(url.format('Lucena City', api_key)).json()
    bayan = requests.get(url.format('Tayabas City', api_key)).json
    print(bayan)
    weather_forecast = {
        'name': r['name'],
        'temperature': r['main']['temp'],
        'icon': r['weather'][0]['icon'],
        'description': r['weather'][0]['description'],
        'pressure': r['main']['pressure']
    }
    print(r)
    return render(request, template_name='weather_forecast/main.html', context={'weather_forecast': weather_forecast})

    