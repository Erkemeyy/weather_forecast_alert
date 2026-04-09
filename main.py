import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

URL ="https://api.openweathermap.org/data/2.5/forecast"
load_dotenv()
weather_forecast ={
    "lat":50.429952,
    "lon":30.4545792,
    "appid": os.getenv("OWM_API_KEY"),
    "cnt": 5
}
my_number = os.getenv("MY_NUMBER")
twilio_number = os.getenv("TWILIO_NUMBER")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def get_weather_with_lat_lon(url, weather_forecast):
    response = requests.get(url, params=weather_forecast)
    response.raise_for_status()
    data = response.json()
    return data

weatherDictForFourDays = get_weather_with_lat_lon(URL, weather_forecast)

will_rain = False
for elements in weatherDictForFourDays["list"]:
    if elements["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        from_=f'whatsapp:{twilio_number}',
        body="It's going to rain today. Remember to bring an umbrella",
        to=f'whatsapp:{my_number}'
    )
else:
    message = client.messages.create(
        from_=f'whatsapp:{twilio_number}',
        body="It's not raining today",
        to=f'whatsapp:{my_number}'
    )


