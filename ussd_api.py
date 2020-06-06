from flask import Flask, Response,stream_with_context, request, session
# from werkzeug.datastructures import Headers
# from werkzeug.exceptions import HTTPException
from io import StringIO
import json
import requests
import hashlib
import hmac
from urllib.parse import urlencode
import re
from bson import json_util
import uuid
import math
import csv
import numbers
import sample
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

app.register_blueprint(sample.routes)

app.secret_key = '&west&south'
app.config['SECRET_KEY'] = 'a98-!_(0)45qurneen'

@app.route('/', methods=['GET'])
def server_status():
    return ' Server running!'



def make_response(code, message):
    if code == '1':
        status = 200
    elif code == '0':
        status = 401
    return Response(response=json.dumps({
        'code': code, 'message': message},
        default=json_util.default),
        status=status,
        mimetype="application/json")

def make_ussd_response(response, statusCode):
  return Response(response=json.dumps(response,
      default=json_util.default),
      status=statusCode,
      mimetype="application/json")

def content_type_response(data):
    return Response(response=json.dumps(data,default=json_util.default),status=200,mimetype= 'application/json')






@app.errorhandler(500)
def server_error(e):
    
    return Response(response=\
    json.dumps({'error':'Internal Server Error! Contact Admin'},\
        default=json_util.default),status=500,\
            mimetype= 'application/json')
    

@app.errorhandler(404)
def page_not_found(e):
    return json.dumps({"error": "Page Not Found"}), 404

@app.errorhandler(400)
def json_format(e):
    return json.dumps({"error": "incorrect json object!"}), 400

# get app version
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=False)
