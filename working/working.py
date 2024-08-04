import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^((\d+:\d+|\d+)\s+(AM|PM))\sto\s((\d+:\d+|\d+)\s+(AM|PM))+", s, re.IGNORECASE)
    hour_1, hour_2 = matches.group(2, 3), matches.group(5, 6)
    return f"{hour_1} to {hour_2}"



def find_am_pm(n, s):
    if s.lower() == "am":
        return f"{int(n)} AM"
    if s.lower() == "pm":
        return f"{(int(n) + 12)} PM"




if __name__ == "__main__":
    main()
