""" jsonrestructure.py - harness for parallel processing json files
"""
import json
import time
from weatherjson import WeatherJSON
from flightjson import FlightJSON

def main():
    """ Main function for program
    """
    wfile = list[WeatherJSON]
    startweather = time.time()
    with open("weather.json", encoding="utf-8") as f:
        wfile = [WeatherJSON(**json.loads(row)) for row in f]

    for we in wfile:
        print(f"High Temp: {we.MaxTemp}")
    stopweather = time.time()
    print(f"Weather processing including printing: {stopweather-startweather:.4f}s")

    startflights = time.time()
    ffile = list[FlightJSON]
    with open("flights-1m.json", encoding="utf-8") as f:
        ffile = [FlightJSON(**json.loads(row)) for row in f]

    print(f"Flight data for row 1234: {ffile[1234-1]}")
    print(
        f"Formatted date for the same record: {ffile[1234-1].FL_DATE.strftime('%m/%d/%Y')}")
    stopflights = time.time()

    print(f"Fights processing including printing one row: {stopflights-startflights:.4f}s")


if __name__ == "__main__":
    main()
