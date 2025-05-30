""" flightjson.py
"""
from dataclasses import dataclass
import datetime

@dataclass
class FlightJSON:
    """ FlightJSON class
    """
    # pylint: disable=invalid-name
    FL_DATE: datetime.date
    DEP_DELAY: int
    ARR_DELAY: int
    AIR_TIME: int
    DISTANCE: int
    DEP_TIME: float
    ARR_TIME: float

    def __post_init__(self):
        if isinstance(self.FL_DATE, str):
            self.FL_DATE = datetime.datetime.strptime(str(self.FL_DATE), "%Y-%m-%d") # type: ignore
