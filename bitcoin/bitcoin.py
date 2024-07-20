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
        return bitcoin


def get_bitcoin_rate():

    argument_json = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = argument_json.json()
    return o["bpi"]["USD"]["rate_float"]


def bitcoin_value():

    amount = get_bitcoin_rate() * get_argument()
    return print(f"${amount:,.4f}")


def main():
    bitcoin_value()


if __name__ == "__main__":
    main()
