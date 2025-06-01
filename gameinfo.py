"""gamestructure.py
"""
from typing import Any
from dataclasses import dataclass

@dataclass
class Armor:
    """ class Armor
    """
    _head: str
    _arms: str
    _chest: str
    _leg: str
    _classitem: str

    @staticmethod
    def from_dict(obj: Any) -> 'Armor':
        """ from_dict - function for unpacking JSON

        Args:
            obj (Any): Dict entry for Armor

        Returns:
            Armor: Armor Class
        """
        _head = str(obj.get("head"))
        _arms = str(obj.get("arms"))
        _chest = str(obj.get("chest"))
        _leg = str(obj.get("leg"))
        _classitem = str(obj.get("classitem"))
        return Armor(_head, _arms, _chest, _leg, _classitem)


@dataclass
class Characteristics:
    """ Characteristics Class

    Returns:
        _type_: Class to support the Characteristics JSON object
    """
    _race: str
    _class: str
    _subclass: str
    _power: int
    _playercountry: str

    @staticmethod
    def from_dict(obj: Any) -> 'Characteristics':
        """ from_dict - function for unpacking JSON

        Args:
            obj (Any): Dict entry for Characteristics

        Returns:
            Characteristics: Characteristics Class
        """
        _race = str(obj.get("race"))
        _class = str(obj.get("class"))
        _subclass = str(obj.get("subclass"))
        _power = int(obj.get("power"))
        _playercountry = str(obj.get("playercountry"))
        return Characteristics(_race, _class, _subclass, _power, _playercountry)


@dataclass
class Location:
    """ Location Class

    Returns:
        _type_: Class to support the Location JSON object
    """
    _map: str
    _waypoint: str

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        """ from_dict - function for unpacking JSON

        Args:
            obj (Any): Dict entry for Location

        Returns:
            Location: Location Class
        """
        _map = str(obj.get("map"))
        _waypoint = str(obj.get("waypoint"))
        return Location(_map, _waypoint)

@dataclass
class ArsenalAttrs():
    """ ArsenalAttrs Class

    Returns:
        _type_: Class to support the ArsenalAttrs of the
                Arsenal JSON object
    """
    _name: str
    _type: str
    _power: int
    _element: str

    @staticmethod
    def from_dict(obj: Any) -> 'ArsenalAttrs':
        """ from_dict - function for unpacking JSON

        Args:
            obj (Any): Dict entry for the attributes of Arsenal

        Returns:
            ArsenalAttrs: ArsenalAttrs Class
        """
        _name = str(obj['name'])
        _type = str(obj['type'])
        _power = int(obj['power'])
        _element = str(obj['element'])

        return ArsenalAttrs(_name, _type, _power, _element) # type: ignore

@dataclass
class Arsenal():
    """ Arsenal Class

    Returns:
        _type_: Class to support the Arsenal JSON object
    """
    _kinetic: ArsenalAttrs
    _energy: ArsenalAttrs
    _power: ArsenalAttrs

    @staticmethod
    def from_dict(obj: Any) -> 'Arsenal':
        """ from_dict - function for unpacking JSON

        Args:
            obj (Any): Dict entry for Arsenal

        Returns:
            Arsenal: Arsenal Class
        """
        _kinetic = ArsenalAttrs.from_dict(obj["kinetic"])
        _energy = ArsenalAttrs.from_dict(obj["energy"])
        _power = ArsenalAttrs.from_dict(obj["power"])

        return Arsenal(_kinetic, _energy, _power)

@dataclass
class Player:
    """ Player Class

    Returns:
        _type_: Class to support the Player JSON object
    """
    _username: str
    _characteristics: Characteristics
    _arsenal: list[Arsenal] | Arsenal
    _armor: Armor
    _location: Location

    @staticmethod
    def from_dict(obj: Any) -> 'Player':
        """ from_dict - function for unpacking JSON

        Args:
            obj (Any): Dict entry for Player

        Returns:
            Player: Player Class
        """
        _username = str(obj.get("username"))
        _characteristics = Characteristics.from_dict(
            obj.get("characteristics"))
        arsenalcheck: list[Arsenal] | Arsenal = obj.get("arsenal")
        if isinstance(arsenalcheck, list):
            _arsenal = [Arsenal.from_dict(a) for a in arsenalcheck]
        else:
            _arsenal = Arsenal.from_dict(arsenalcheck)
        _armor = Armor.from_dict(obj.get("armor"))
        _location = Location.from_dict(obj.get("location"))
        return Player(_username, _characteristics, _arsenal, _armor, _location)

@dataclass
class PerPlayer:
    """ PerPlayer Class

    Returns:
        _type_: Class to support the PerPlayer JSON object
    """
    #pylint: disable=invalid-name
    _requestNo: str
    _Batch_Number: str
    _Total_No_Of_Batches: str
    _player: list[Player]

    @staticmethod
    def from_dict(obj: Any) -> 'PerPlayer':
        """ from_dict - function for unpacking JSON

        Args:
            obj (Any): Dict entry for PerPlayer

        Returns:
            PerPlayer: PerPlayer Class
        """
        _requestNo = str(obj.get("requestNo"))
        _Batch_Number = str(obj.get("Batch_Number"))
        _Total_No_Of_Batches = str(obj.get("Total_No_Of_Batches"))
        _player = [Player.from_dict(y) for y in obj.get("player")]
        return PerPlayer(_requestNo, _Batch_Number, _Total_No_Of_Batches, _player)


@dataclass
class GameInfo():
    """ GameInfo Class

    Returns:
        _type_: Class to support the GameInfo JSON object
    """
    # pylint: disable=invalid-name
    _PerPlayer: PerPlayer

    @staticmethod
    def from_dict(obj: Any) -> 'GameInfo':
        """ from_dict - function for unpacking JSON

        Args:
            obj (Any): Dict entry for GameInfo

        Returns:
            GameInfo: GameInfo Class
        """
        _PerPlayer = PerPlayer.from_dict(obj.get("PerPlayer"))
        return GameInfo(_PerPlayer)
