from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import logging
import payloadParser

app = Flask(__name__)
CORS(app)
api = Api(app)

logging.basicConfig(
    
    format="%(message)s level=%(levelname)-7s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

@app.route('/', methods=["GET"])
def get():

    result = {'data': 'Hello... 404'}
    return jsonify(result)


@app.route('/hackernews', methods=["GET"])
def exec_indecon():    
        
    parser = payloadParser.PayloadParser()
    resp = parser.getHackernews()

    response = jsonify(resp)
    return response, 200

if __name__ == '__main__':
     app.run(port='8085', host='0.0.0.0', debug=True)

