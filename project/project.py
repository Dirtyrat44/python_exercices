import requests
import re
import json

def main():
    response = requests.get("https://openfarm.cc/api/v1/crops?filter=tomato")
    o = response.json()
    for attributes in o["attributes"]:
        print(attributes)


def input_check():
    ...


if __name__ == "__main__":
    main()
