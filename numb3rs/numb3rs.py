import re
import sys


def main():
    validate(input("IPv4 Address: "))


def validate(ip):
    if result :=re.search(r"^\b+\.\b+\.\b+\.\b+$", ip):
        sys.exit("True")
        print(result)

    else:
        sys.exit("False")


...


if __name__ == "__main__":
    main()
