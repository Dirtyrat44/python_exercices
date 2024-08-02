import re
import sys


def main():
    validate(input("IPv4 Address: "))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)", ip)
    if matches:
        print(matches.group(1))
        sys.exit("True")

    else:
        sys.exit("False")





if __name__ == "__main__":
    main()
