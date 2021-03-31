import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, Response
from dotenv import load_dotenv
from pyowm import OWM
from pyowm.utils.config import get_default_config
from flask_sqlalchemy import SQLAlchemy
from models import Historico

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")

# config_dict = get_default_config()
# config_dict['language'] = 'pt'



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# own = OWM(settings.API_KEY, config_dict)
# mgr = own.weather_manager()
# reg = own.city_id_registry()

# @app.route('/')
# def hello():
#     # observation = mgr.weather_at_place('Fortaleza,BR-CE')
#     # w = observation.weather
#     list_of_string = " ".join([str(elem) for elem in reg.ids_for('London')])
#     return list_of_string



