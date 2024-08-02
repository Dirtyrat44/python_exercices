import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        if check_number(matches.group(1)) and check_number(matches.group(2)) and check_number(matches.group(3)) and check_number(matches.group(4)):
            return "True"
        else:
            return"False"

    else:
        return "False"

def check_number(n):
    try:
        n = int(n)
    except ValueError:
        return None
    else:
        return 0 <= n <= 255



if __name__ == "__main__":
    main()
