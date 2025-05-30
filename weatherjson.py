""" weatherjson.py
"""
from dataclasses import dataclass

@dataclass
class WeatherJSON:  # pylint: disable=too-many-instance-attributes
    """ WeatherJSON class
    """
    # pylint: disable=invalid-name
    MinTemp: float
    MaxTemp: float
    Rainfall: float
    Evaporation: float
    Sunshine: float
    WindGustDir: str
    WindGustSpeed: float
    WindDir9am: str
    WindDir3pm: str
    WindSpeed9am: float
    WindSpeed3pm: float
    Humidity9am: float
    Humidity3pm: float
    Pressure9am: float
    Pressure3pm: float
    Cloud9am: int
    Cloud3pm: int
    Temp9am: float
    Temp3pm: float
    RainToday: str
    RISK_MM: int
    RainTomorrow: str
