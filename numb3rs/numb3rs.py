import re
import sys


def main():
    validate(input("IPv4 Address: "))


def validate(ip):
    if matches := re.search(r"^(\d+)\.(\d+)\.\(d+)\.(\d+)$", ip):
        print(matches.groups(1))
        sys.exit("True")

    else:
        sys.exit("False")





if __name__ == "__main__":
    main()
