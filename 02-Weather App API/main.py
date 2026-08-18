from fastapi import FastAPI, Query, HTTPException
import requests
#from app.config import WEATHER_API_KEY
from urllib.parse import quote
app = FastAPI()

API_KEY = "apikey"

@app.get('/weather')
def get_weather(zip_code = Query("23607", examples=["23607"])):
    
    #encoded_zip = quote(zip_code)
    
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"f"{zip_code}?unitGroup=us&key={API_KEY}&contentType=json"
    
    response = requests.get(url)
    data = response.json()
    
    
    
    return{
        "city": str(data["resolvedAddress"]),
        "temperature": float(data["currentConditions"]["temp"]),
        "humidity": float(data["currentConditions"]["humidity"]),
        "description": str(data["currentConditions"]["conditions"])     
    }

