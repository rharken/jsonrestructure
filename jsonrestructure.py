""" jsonrestructure.py - harness for parallel processing json files
"""
import json
import time

def main():
    """ Main function for program
    """
    startrestructure = time.time()
    with open("gamedata.json", encoding="UTF8") as f:
        for row in f:
            rowjson = json.loads(row)
            print(rowjson)

            for player in rowjson['PerPlayer']['player']:
                print(f"username: {player['username']}")
                for characteristic in player['characteristics']:
                    print(f"\t{characteristic}: {player['characteristics'][characteristic]}")

    stoprestructure = time.time()
    print(f"Processing time: {stoprestructure-startrestructure:.4f}s")


if __name__ == "__main__":
    main()
