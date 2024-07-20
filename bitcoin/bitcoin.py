import sys
import requests
import json


def get_argument():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        return sys.argv[1]

def get_bitcoin_rate():
    argument = get_argument()
    argument_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = argument_json.json()
    return rate_float = o["bpi"]["USD"]["rate_float"]

def main():
    ...






if __name__ == "__main__":
    main()
