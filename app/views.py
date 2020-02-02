from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.core.paginator import Paginator

from .forms import CityForm, HistoryFilterForm
from .utils import OpenWeatherAPI
from .models import Weather, City

import json

# Create your views here.

def index(request):
    context = dict()
    context['meta'] = {
        'main_bar_button' : 'active'
    }
    city_form = CityForm()
    context['form'] = {
        'city' : city_form
    }
    if request.method == 'GET':
        return render(request, 'app/index.html', context=context)
    if request.method == 'POST':
        city = request.POST['name']
        context['city'] = city
        weather = OpenWeatherAPI.get_weather_in(city)
        if weather:
            to_insert = {
                'city' : City.objects.filter(name=weather['name'])[0],
                'temp' :  weather['temp'],
                'wind_speed' :  weather['wind_speed'],
                'wind_deg' :   weather['wind_deg'],
                'sky' :  weather['sky'],
                'icon' :  weather['icon'],
            } 
            Weather(**to_insert).save()
            context['weather'] = weather
        else:
            context['error'] = 'Wheather for this city not finded'
        return render(request, 'app/index.html', context=context)    
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])



def history(request):
    items_per_page = 10
    context = dict()
    context['meta'] = {
        'history_bar_button' : 'active'
    }
    page = request.GET['page'] if 'page' in request.GET else 1
    if request.method == 'GET':
        args = request.GET
        if set(args.keys()).intersection(['name', 'date_from', 'date_to']):
            context['form'] = {
                'filter' : HistoryFilterForm(initial={ 'name' : args['name'], 
                'date_from' : args['date_from'],
                'date_to' : args['date_to'],
                 })
            }
            data = Weather.objects.filter(city__name__startswith=args['name'])
            if args['date_from']:
                data = data.filter(date__gte=args['date_from'])
            if args['date_to']:
                data = data.filter(date__lte=args['date_to'])
        else:
            context['form'] = {
                'filter' : HistoryFilterForm()
            }
            data = Weather.objects.all()
        paginator = Paginator(data, items_per_page)
        page_obj = paginator.get_page(page)
        context['page_obj'] = page_obj

        form_state = str()
        for key in args:
            if key != 'page':
                form_state += f'&{key}={args[key]}'
        context['state'] = form_state
        return render(request, 'app/history.html', context=context)
    else:
        return HttpResponseNotAllowed(["GET", "POST"])


def cities(request, symbol):
    print(symbol)
    data = City.objects.filter(name__contains=symbol)
    return HttpResponse(
        json.dumps(
            [
                {
                    'name' : item.name,
                    'country' : item.country
                }
                for item in data
            ] 
        ))
