import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^((\d+:\d+|\d+)\s+(AM|PM))\s+to\s+((\d+:\d+|\d+)\s+(AM|PM))+", s, re.IGNORECASE)
    if matches:
        hour_1, am_pm_1, hour_2, am_pm_2 = matches.group(1, 2, 3, 4)
        return f"{hour_1} to {hour_2}"



def find_am_pm(n, s):





if __name__ == "__main__":
    main()
