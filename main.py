import requests
import os
from dotenv import  load_dotenv, dotenv_values


city = "Kyiv"
lat="50.447731"
lon="30.542721"
URL ="https://api.openweathermap.org/data/2.5/forecast"
load_dotenv()
weather_forecast ={
    "lat":50.429952,
    "lon":30.4545792,
    "appid": os.getenv("API_KEY"),
    "cnt": 4
}

def get_weather_with_lat_lon(url, weather_forecast):
    response = requests.get(url, params=weather_forecast)
    data = response.json()
    status_code = response.status_code
    print(status_code)
    return data

weatherDictForFourDays = get_weather_with_lat_lon(URL, weather_forecast)

will_rain = False
for elements in weatherDictForFourDays["list"]:
    if elements["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
# print(get_weather_with_lat_lon(url, weather_forecast).get("list")[0].get("weather")[0].get("id"))

