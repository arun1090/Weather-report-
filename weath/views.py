from django.shortcuts import render
import requests
from .forms import CityForm
from .models import City
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

def index(request):
    API_KEY = '03f67a87287862fd5b36c4eb78cff5b8'
    city= 'London'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city},uk&appid={API_KEY}'
    city_weather = requests.get(url).json()
    print(city_weather)
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    context = {'weather': weather}
    return render(request, 'weath/index.html', context,)

@csrf_exempt

def weather_view(request):
    C1=CityForm()
    context={}
    if request.method=='POST':
        C1=CityForm(request.POST)
        print('post in')
      #  data=request.POST
        C1.save()
        C1=CityForm()
        print('C1 saved to database ')
      #  print(data)
      #  city=data['name']
      #  print(city)
        cities = City.objects.all().order_by('-id')[:4]
        print(cities)
        weather_data=[]
        for city in cities:
            print(city)
            API_KEY = '03f67a87287862fd5b36c4eb78cff5b8'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
            print(url)
            city_weather = requests.get(url).json()
            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)

        context = {'weather': weather_data, "form":C1}
        print(C1)
        return render(request, 'weath/index.html', context,)
    else:

        return render(request, 'weath/index.html', {"form": C1})

    return render(request, 'weath/index.html', {"form":C1})






# Create your views here.
