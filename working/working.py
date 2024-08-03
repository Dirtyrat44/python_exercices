import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search("^((\d+|\d+:\d+)\s+(AM|PM))", s, re.IGNORECASE)
    return matches.group(1)



def find_am_pm(s):
    matches = re.search("^((\d+|\d+:\d+)\s+(AM|PM))", s, re.IGNORECASE)
    return matches.group(1)


if __name__ == "__main__":
    main()
