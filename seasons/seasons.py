from datetime import date
import inflect  # translate numbers to words
import sys

p = inflect.engine()
# words = p.number_to_words(1234, andword="")
# "one thousand, two hundred thirty-four"


def main():
    print(date_input_format())

def time_range(time):
    ...

def date_input_format():
    birth = input("Date of birth: ").split("-")
    return date(*map(int, birth))


if __name__ == "__main__":
    main()
