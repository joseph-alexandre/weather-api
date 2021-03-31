from dotenv import load_dotenv
from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import TimeoutError
import os

config_dict = get_default_config()
config_dict['language'] = 'pt'

owm = OWM(os.environ.get("API_KEY"), config_dict)
mgr = owm.weather_manager()
reg = owm.city_id_registry()
