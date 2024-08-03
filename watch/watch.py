import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r'https?://(?:www\.)?youtube.com/embed/(.+)(?=")', s)
    return matches.group(1)





if __name__ == "__main__":
    main()
