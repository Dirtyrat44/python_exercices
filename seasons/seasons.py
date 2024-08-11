from datetime import date

import inflect  # translate numbers to words
import sys

p = inflect.engine()
# words = p.number_to_words(1234, andword="")
# "one thousand, two hundred thirty-four"


def main():
    user_birth = check_date_format(input("Date of birth: "))
    days_difference = date.today() - user_birth
    minutes_difference = (lambda x: 1440 * x.days)(days_difference)
    words = p.number_to_words(minutes_difference, andword="")
    print(f"{words.capitalize()} minutes")


def check_date_format(date_str):

    if len(date_str) != 3:
        sys.exit("Invalid date")
    birth = date_str.split("-")
    year, month, day = birth
    if not year.isdigit() and not month.isdigit() and not day.isdigit():
        sys.exit("Invalid date")
    year, month, day = int(year), int(month), int(day)
    if not 0 < year <= 9999:
        sys.exit("Invalid date")
    if not 0 < month <= 12:
        sys.exit("Invalid date")

    if month in [1, 3, 5, 7, 8, 10, 12] and not 0 < day <= 31:
        sys.exit("Invalid date")
    if month in [4, 6, 9, 11] and not 0 < day <= 30:
        sys.exit("Invalid date")
    # check january month's days
    if month == 2:
        if year % 2 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    if not 0 < day <= 29:
                        sys.exit("Invalid date")
                else:
                    if not 0 < day <= 28:
                        sys.exit("Invalid date")
            else:
                if not 0 < day <= 29:
                    sys.exit("Invalid date")
        else:
            if not 0 < day <= 28:
                sys.exit("Invalid date")

    return date(year, month, day)


if __name__ == "__main__":
    main()
