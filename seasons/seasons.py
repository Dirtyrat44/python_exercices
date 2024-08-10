from datetime import date
import inflect  # translate numbers to words
import sys

p = inflect.engine()
# words = p.number_to_words(1234, andword="")
# "one thousand, two hundred thirty-four"


def main():
    birth = input("Date of birth: ").split("-")
    print(convert_date(birth))

def time_range(time):
    ...

def convert_date(d):
    return date(*map(int, d))


if __name__ == "__main__":
    main()
