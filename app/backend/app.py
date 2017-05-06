from flask import Flask
from flask_cors import CORS, cross_origin
from flask_restful import Api

from api.hello import HelloWorld
from api.health import Health

app = Flask(__name__)
api = Api(app)

CORS(app)

api.add_resource(Health, '/health')
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)