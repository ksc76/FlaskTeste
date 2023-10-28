from flask import Flask
from src.controllers import *


routes={
    'olarota':'/',
    'olacontroller':'OlaController'.as_view('ola')
    }

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"