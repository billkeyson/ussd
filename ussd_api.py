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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=False)
