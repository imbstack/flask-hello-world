import os
import requests
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return requests.get(os.environ["UPSTREAM"]).text
