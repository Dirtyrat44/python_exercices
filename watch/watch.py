import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"https?", s)
    print(matches)





if __name__ == "__main__":
    main()
