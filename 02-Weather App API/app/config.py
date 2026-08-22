import os

from dotenv import find_dotenv, load_dotenv

dotenv_path = load_dotenv()

WEATHER_API_KEY = os.getenv("API_KEY")