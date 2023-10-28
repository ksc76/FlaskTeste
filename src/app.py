from flask import Flask
from src.routes import routes

app = Flask(__name__)

app.add_url_rule(routes['olarota'], view_func=['olacontroller'])