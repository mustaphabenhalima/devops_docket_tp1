import requests
import json
from datetime import datetime as dt
import os
api_key = os.environ['API_KEY']
lat = os.environ['LAT']
lon = os.environ['LONG']
url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
res = requests.get(url)
dt = json.loads(res.text)
print(dt)