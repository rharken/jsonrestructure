""" gamerestructure.py - restructure of complex json
"""
import json
from gameinfo import GameInfo

def main():
    """ Main function
    """

    with open("gamedata.json", encoding="UTF-8") as f:
        jsonobj = [json.loads(row) for row in f]

    for p in jsonobj:
        gameinfo = GameInfo.from_dict(p)
        print(gameinfo)
        for player in gameinfo._PerPlayer._player: # type: ignore # pylint: disable=protected-access
            print(player._username)                # type: ignore # pylint: disable=protected-access

if __name__ == "__main__":
    main()
