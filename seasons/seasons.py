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
    year, month, day = birth
    if not 0 < year <= 9999:
        sys.exit("Invalid date")
    if not 0 < month <= 12:
        sys.exit("Invalid date")


    #day bissexstile ou pas

    if day in [1, 3, 5, 7, 8, 10, 12]

def date_input_format():
    return date(*map(int, birth))


if __name__ == "__main__":
    main()
