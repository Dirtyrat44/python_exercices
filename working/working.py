import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"/^([0-9][0-2]?)(:[0-5][0-9])? (AM|PM) to ([0-9][0-2]?)(:[0-5][0-9])? (AM|PM)$/gm", s)
    if matches:
        ...
    else:
        raise ValueError


def convert_to_24_hour():
    


if __name__ == "__main__":
    main()
