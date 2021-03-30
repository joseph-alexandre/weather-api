import os
from os.path import join, dirname
from dotenv import load_dotenv
from pyowm import OWM
from pyowm.utils.config import get_default_config



dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")

API_URL_PART_1 = "api.openweathermap.org/data/2.5/forecast?q="

API_URL_PART_2 = "&appid=" + API_KEY



