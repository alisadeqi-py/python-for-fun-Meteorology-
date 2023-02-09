import requests
from base import WeatherApi

class OpenMeteo(WeatherApi):
    def __init__(self,latitude,longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_current_temprature(latitude, longitude):
        result = requests.get('https://api.open-meteo.com/v1/forecast' , params={'latitude': latitude, 'longitude': longitude , 'current_weather' : True})
        J_result = result.json()
        return J_result['current_weather']['temperature']

