from fastapi import FastAPI, Query, HTTPException
import requests
from urllib.parse import quote
from app.config import WEATHER_API_KEY

app = FastAPI()

API_KEY = WEATHER_API_KEY



@app.get('/weather')
def get_weather(zip_code = Query("23607", examples=["23607"])):
    
    if not WEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="API key not configured")
    
    
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"f"{zip_code}?unitGroup=us&key={API_KEY}&contentType=json"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Zip not found or weather service unavailable. Please confirm the Zip Code and try again.")
    
    data = response.json()
    
    return{
        "city": str(data["resolvedAddress"]),
        "temperature": float(data["currentConditions"]["temp"]),
        "humidity": float(data["currentConditions"]["humidity"]),
        "description": str(data["currentConditions"]["conditions"])     
    }

