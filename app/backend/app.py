from flask import Flask
from flask_cors import CORS, cross_origin
from flask import jsonify

app = Flask(__name__)
CORS(app)


@app.route('/health')
def health():
    return 'Ok'

@app.route('/')
def hello():
	return "Hello World"