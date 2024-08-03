import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


def find_am_pm(s):
    matches = re.search("^([0-9]|(1[10-2])", s, re.IGNORECASE)


if __name__ == "__main__":
    main()
