from flask_restful import Resource
import requests
from flask_restful import output_json

class Weather(Resource):
    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, city):
        r = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}".format(city=city, appid=self.api_key))
        if r.status_code == 200:
            return output_json(r.json(), r.status_code)
        else:
            return {}, r.status_code
