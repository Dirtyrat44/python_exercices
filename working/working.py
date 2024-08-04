import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"/^([0-9][0-2]?):?([0-5][0-9])? (AM|PM) to ([0-9][0-2]?):?([0-5][0-9])? (AM|PM)$/gm", s)
    if matches:
        hour_1, minute_1, am_pm_1 = matches.group(1, 2, 3)
        hour_2, minute_2, am_pm_2 = matches.group(4, 5, 6)
        new_time_1 = convert_to_24_hour(hour_1, minute_1, am_pm_1)
        new_time_2 = convert_to_24_hour(hour_2, minute_2, am_pm_2)
        return f"{new_time_1} to {new_time_2}"
    else:
        raise ValueError


def convert_to_24_hour(hour, minute, am_pm):
    if am_pm == "AM":
        if int(hour) == 0:
            raise ValueError
        if int(hour) == 12:
            return


if __name__ == "__main__":
    main()
