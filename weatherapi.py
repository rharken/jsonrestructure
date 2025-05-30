""" weatherapi.py
"""
import os
import json
import requests
import dotenv
from weatherapidata import WeatherAPIData

dotenv.load_dotenv()

def main():
    """ Main function for weatherpi.py
    """
    api_key: str = str(os.getenv("API_KEY", ""))
    geo_code: str = str(os.getenv("GEO_CODE", ""))

    url: str = "https://api.weather.com/v3/wx/forecast/daily/5day"

    querystring: dict[str, str] = {"geocode": geo_code, "format": "json", "units": "e",
                               "language": "en-US", "apiKey": api_key}

    payload: str = ""
    response: requests.Response = requests.request("GET", url,
                                                   data=payload,
                                                   params=querystring,
                                                   timeout=5)
    #print(response.text)

    if response:
        forecast = WeatherAPIData(**json.loads(response.text))
        #print(forecast)

        for i in range(6):
            print(f"moonrise: {forecast.moonriseTimeLocal[i]}"
                  f"  moonset: {forecast.moonsetTimeLocal[i]}")

        for li in forecast.daypart:
            for i in range(12):
                print(f"{li['daypartName'][i]}: {li['narrative'][i]}")


if __name__ == "__main__":
    main()
