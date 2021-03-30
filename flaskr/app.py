from flask import Flask, render_template
from dotenv import load_dotenv
import settings
import requests
from pyowm import OWM
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'pt'



app = Flask(__name__, template_folder='templates')
own = OWM(settings.API_KEY, config_dict)
mgr = own.weather_manager()
reg = own.city_id_registry()


@app.route('/')
def hello():
    # observation = mgr.weather_at_place('Fortaleza,BR-CE')
    # w = observation.weather
    list_of_string = " ".join([str(elem) for elem in reg.ids_for('London')])
    return list_of_string


if __name__ == "__main__":
    app.run()