""" weatherapi.py
"""
import os
import json
from dataclasses import make_dataclass
import dotenv
import requests

dotenv.load_dotenv()

API_KEY: str = str(os.getenv("API_KEY", ""))
GEO_CODE: str = str(os.getenv("GEO_CODE", ""))

URL = "https://api.weather.com/v3/wx/forecast/daily/5day"

querystring = {"geocode": GEO_CODE, "format": "json", "units": "e",
               "language": "en-US", "apiKey": API_KEY}

PAYLOAD = ""
response = requests.request("GET", URL, data=PAYLOAD, params=querystring, timeout=5)

#print(response.text)

my_dict = json.loads(response.text)

MyDynamicallyCreatedDataclass = make_dataclass(
    "MyDynamicallyCreatedDataclass", ((k, type(v)) for k, v in my_dict.items()) # type: ignore
)(**my_dict)

print(MyDynamicallyCreatedDataclass.__annotations__)
