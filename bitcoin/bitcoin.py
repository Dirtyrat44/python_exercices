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


def main():
    argument = get_argument()
    argument_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(argument_json.raise_for_status())
    print(argument_json)



if __name__ == "__main__":
    main()
