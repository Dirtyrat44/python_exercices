from datetime import date
import inflect  # translate numbers to words
import sys

p = inflect.engine()
# words = p.number_to_words(1234, andword="")
# "one thousand, two hundred thirty-four"


def main():
    check_date_format()

def check_date_format():
    birth = input("Date of birth: ").split("-")
    int(birth)
    print(birth)

def date_input_format():
    birth = input("Date of birth: ").split("-")
    year, month, day = birth
    return date(*map(int, birth))


if __name__ == "__main__":
    main()
