import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ...


def find_am_pm(s):
    matches = re.search("^((\d+):?(\d+)?\s+(AM|PM))", s, re.IGNORECASE)


if __name__ == "__main__":
    main()
