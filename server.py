from flask import Flask
from flask import request
from flask_cors import CORS
import json
import requests
import codecs
from requests.auth import HTTPBasicAuth
from graph_builder import GraphBuilder
from flask import jsonify

app = Flask(__name__)
# Load configs from file. File path must be set using command `export APP_SETTINGS=path/to/config.cfg
app.config.from_envvar('APP_SETTINGS')
CORS(app)

config = {}
redis_host = app.config.get('REDIS_HOST')
redis_port = app.config.get('REDIS_PORT')
graph_builder = GraphBuilder(redis_host, redis_port, verse_similarity)

print("Initialization complete")
@app.route('/')
def home():
    return 'Wikifier implementation'

@app.route('/get_identifiers', methods=['POST'])
def get_identifiers():
    request_data = json.loads(request.data)
    data = graph_builder.get_identifiers(request_data)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
return response
