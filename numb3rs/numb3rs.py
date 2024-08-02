import re
import sys


def main():
    validate(input("IPv4 Address: "))


def validate(ip):
    if re.search(r"^+", ip):
        sys.exit("True")

    else:
        sys.exit("False")


...


if __name__ == "__main__":
    main()
