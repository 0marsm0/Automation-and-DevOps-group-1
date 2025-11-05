import requests
import json
import pandas as pd
from datetime import datetime, timedelta

def get_weather(lat=59.33, lon=18.06):

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m",
        "timezone": "Europe/Stockholm"
    }

    respons = requests.get(url, params=params).json()


    df = pd.DataFrame({
    "time": pd.to_datetime(respons["hourly"]["time"]),
    "temperature": respons["hourly"]["temperature_2m"]
    })
 
 
    now = datetime.now()
    next_24h = now + timedelta(hours=24)
    df_24 = df[(df["time"] >= now) & (df["time"] <= next_24h)].reset_index()
    df_24 = df_24.drop(["index"], axis=1)

    return df_24


if __name__ == "__main__":
    get_weather()