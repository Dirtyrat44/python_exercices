import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"https?://(?:www\.)?youtube.com/embed/(.+)", s)
    print(matches.group1)
    print(matches)





if __name__ == "__main__":
    main()
