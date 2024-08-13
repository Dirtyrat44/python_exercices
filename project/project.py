import requests
import re
import json

def main():
    response = requests.get("https://openfarm.cc/api/v1/crops?filter=carrot")
    o = response.json()
    print(json.dumps(response.json(), indent=4))

def input_check():
    ...


if __name__ == "__main__":
    main()
