""" weatherapidata.py
"""
from dataclasses import dataclass
import datetime
from typing import TypedDict


class DaypartDict(TypedDict):
    """ DaypartDict - Dictionary found in daypart list

    Args:
        TypedDict (_type_): Typed Dictionary
    """
    cloudcover: list[int]            # Dict key: 'cloudcover'
    dayornight: list[str]            # Dict key: 'dayornight'
    daypartName: list[str]           # Dict key: 'daypartName'
    iconCode: list[int]              # Dict Key: 'iconCode'
    iconCodeExtend: list[int]        # Dict Key: 'iconCodeExtend'
    narrative: list[str | None]      # Dict Key: 'narrative'
    precipChance: list[int]          # Dict Key: 'precipChance'
    precipType: list[str]            # Dict Key: 'precipType'
    qpf: list[float]                 # Dict Key: 'qpf'
    qpfSnow: list[float]             # Dict Key: 'qpfSnow'
    qualifierCode: list[str]         # Dict Key: 'qualifierCode'
    qualifierPhrase: list[str]       # Dict Key: 'qualifierPhrase'
    relativeHumidity: list[int]      # Dict Key: 'relativeHumidity'
    snowRange: list[str]             # Dict Key: 'snowRange'
    temperature: list[int]           # Dict Key: 'temperature'
    temperatureHeatIndex: list[int]  # Dict Key: 'temperatureHeadIndex'
    temperatureWindChill: list[int]  # Dict Key: 'temperatureWindChill'
    thunderCategory: list[str]       # Dict Key: 'thunderCategory'
    thunderIndex: list[int]          # Dict Key: 'thunderIndex'
    uvDescription: list[str]         # Dict Key: 'uvDescription'
    uvIndex: list[str]               # Dict Key: 'uvIndex'
    windDirection: list[int]         # Dict Key: 'windDirection'
    windDirectionCardinal: list[str] # Dict Key: 'windDirectionCardinal'
    windPhrase: list[str]            # Dict Key: 'windPhrase'
    windSpeed: list[int]             # Dict Key: 'windSpeed'
    wxPhraseLong: list[str]          # Dict Key: 'wxPhraseLong'
    wxPhraseShort: list[str]         # Dict Key: 'wxPhraseShort'


@dataclass
class WeatherAPIData:  # pylint: disable=too-many-instance-attributes
    """ WeatherAPIData class
    """
    # pylint: disable=invalid-name
    calendarDayTemperatureMax: list[int]
    calendarDayTemperatureMin: list[int]
    dayOfWeek: list[str]
    expirationTimeUtc: list[int]
    moonPhase: list[str]
    moonPhaseCode: list[str]
    moonPhaseDay: list[int]
    moonriseTimeLocal: list[str | datetime.datetime | None]
    moonriseTimeUtc: list[int]
    moonsetTimeLocal: list[str | datetime.datetime | None]
    moonsetTimeUtc: list[int]
    narrative: list[str]
    qpf: list[float]
    qpfSnow: list[float]
    sunriseTimeLocal: list[str | datetime.datetime | None]
    sunriseTimeUtc: list[int]
    sunsetTimeLocal: list[str | datetime.datetime | None]
    sunsetTimeUtc: list[int]
    temperatureMax: list[int]
    temperatureMin: list[int]
    validTimeLocal: list[str | datetime.datetime | None]
    validTimeUtc: list[int]
    daypart: list[DaypartDict]

    def ConvertStrList2Datetime(self,
                                dliststr: list[str | datetime.datetime | None],
                                tmformat: str = "%Y-%m-%dT%H:%M:%S%z"
                                ) -> list[str | datetime.datetime | None]:
        """ ConvertStrList2Datetime - helper function to translate strings to datetime

        Args:
            dliststr (list[str  |  datetime.datetime  |  None]): Initial List
            tmformat (_type_, optional): _description_. Defaults to "%Y-%m-%dT%H:%M:%S%z".

        Returns:
            list[str | datetime.datetime | None]: Replacement list
        """
        newdata: list[str | datetime.datetime | None] = []
        for data in dliststr:
            if isinstance(data, str):
                if data:
                    newdata.append(datetime.datetime.strptime(
                        str(data), tmformat))
                else:
                    newdata.append(None)
            elif isinstance(data, datetime.datetime):
                newdata.append(data)
            else:
                newdata.append(None)
        return newdata

    def __post_init__(self):
        self.moonriseTimeLocal = self.ConvertStrList2Datetime(self.moonriseTimeLocal)
        self.moonsetTimeLocal = self.ConvertStrList2Datetime(self.moonsetTimeLocal)
        self.sunriseTimeLocal = self.ConvertStrList2Datetime(self.sunriseTimeLocal)
        self.sunsetTimeLocal = self.ConvertStrList2Datetime(self.sunsetTimeLocal)
        self.validTimeLocal = self.ConvertStrList2Datetime(self.validTimeLocal)
