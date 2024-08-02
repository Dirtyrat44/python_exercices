import re
import sys


def main():
    validate(input("IPv4 Address: "))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        if check_number(matches.group(1)) and check_number(matches.group(2)) and check_number(matches.group(3)) and check_number(matches.group(4)):
            sys.exit("True")
        else:
            sys.exit("False")

    else:
        sys.exit("False")

def check_number(n):
    n = int(n)
    return 0 <= n <= 255



if __name__ == "__main__":
    main()
