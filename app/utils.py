import requests

from .models import City 

class OpenWeatherAPI:
    API_KEY = '1b5ee5a1a74d624a74750350327ea372'


    @staticmethod
    def get_weather_in(param):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={ param }&appid={ OpenWeatherAPI.API_KEY }'

        respose = requests.get(url) 
        if respose.status_code == 200:
            data = respose.json()
            OpenWeatherAPI.check_city_in_db(data)
            transformed_data = OpenWeatherAPI.transform_data_to_my_format(data)
            return transformed_data
        else:
            return {}   


    @staticmethod
    def transform_data_to_my_format(raw_data):
        # print(raw_data)
        transformed_data = dict()
        transformed_data['name'] = raw_data['name']
        transformed_data['temp'] = raw_data['main']['temp'] - 273.15
        transformed_data['sky'] = raw_data['weather'][0]['main']
        transformed_data['icon'] = raw_data['weather'][0]['icon']
        if 'speed' in raw_data['wind']:
            transformed_data['wind_speed'] = raw_data['wind']['speed']
        else:
            transformed_data['wind_speed'] = 0
        if 'deg' in raw_data['wind']:
            transformed_data['wind_deg'] = raw_data['wind']['deg']
        else:
            transformed_data['wind_deg'] = 0
        transformed_data['clouds'] = raw_data['clouds']['all']
        
        # print(transformed_data)
        return transformed_data


    @staticmethod
    def check_city_in_db(raw_data):
        if not City.objects.filter(name=raw_data['name']):
            sample = {
                'name' : raw_data['name'],
                'country': raw_data['sys']['country'],
                'lat' : raw_data['coord']['lat'], 
                'lon' : raw_data['coord']['lon'], 
            }
            City(**sample).save()



# import json 
# df = json.loads(open('db/city.list.json').read())
# for item in df:
#     sample = {
#         'name' : item['name'],
#         'country': item['country'],
#         'lat' : item['coord']['lat'],
#         'lon' : item['coord']['lon']
#     }
#     City(**sample).save()