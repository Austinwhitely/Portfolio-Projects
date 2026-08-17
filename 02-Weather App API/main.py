from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

weather_data = []

class Weather(BaseModel):
    zip: int 
    high: int = None
    low: int = None

@app.get('/')
def root():
    return{"hello world"}

@app.post('/zip')
def create_item(item: Weather):
    weather_data.append(item)
    return weather_data

