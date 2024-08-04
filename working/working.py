import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^((\d+:\d+|\d+)\s+(AM|PM))\sto\s((\d+:\d+|\d+)\s+(AM|PM))+", s, re.IGNORECASE)
    return matches.group(4)



def find_am_pm(s, n):
    if s.lower() == "am":
        return int(n)
    if s.lower() == "pm":
        return (int(n) + 12)




if __name__ == "__main__":
    main()
