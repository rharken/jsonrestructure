""" gamerestructure.py - restructure of complex json
"""
import json
from gameinfo import GameInfo

def main():
    """ Main function
    """

    with open("gamedata.json", encoding="UTF-8") as f:
#        gameinfo = [GameInfo(**json.loads(r)) for r in f]
        jsonobj = [json.loads(r) for r in f]

    for p in jsonobj:
        gameinfo = GameInfo.from_dict(p)
        print(gameinfo)

if __name__ == "__main__":
    main()
