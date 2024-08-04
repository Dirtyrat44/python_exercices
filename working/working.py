import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^((\d+:\d+|\d+)\s+(AM|PM))\sto\s((\d+:\d+|\d+)\s+(AM|PM))+", s, re.IGNORECASE)
    return matches.group(2)



def find_am_pm(s):
    ...


if __name__ == "__main__":
    main()
