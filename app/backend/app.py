import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from api.health import Health
from api.hello import HelloWorld
from api.weather import Weather

app = Flask(__name__)
api = Api(app)

CORS(app)

weather_api_key = os.environ["WEATHER_API_KEY"]

api.add_resource(Health, '/health')
api.add_resource(HelloWorld, '/')
api.add_resource(Weather, '/weather/<city>', resource_class_kwargs={'api_key': weather_api_key})

if __name__ == '__main__':
    app.run(debug=True)