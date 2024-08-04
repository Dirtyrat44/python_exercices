import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(\d+:\d+|\d+)\s+(AM|PM)\s+to\s+(\d+:\d+|\d+)\s+(AM|PM)$", s, re.IGNORECASE)
    if matches:
        hour_1, am_pm_1, hour_2, am_pm_2 = matches.group(1, 2, 3, 4)
        hour_1_24 = convert_to_24h(hour_1, am_pm_1)
        hour_2_24 = convert_to_24h(hour_2, am_pm_2)
        return f"{hour_1_24} to {hour_2_24}"


def convert_to_24h(time, period):
    hours, minutes = 0, 0
    if ":" in time:
        hours, minutes = map(int, time.split(":"))
    else:
        hours = int(time)

    if period.lower() == "pm" and hours != 12:
        hours += 12
    elif period.lower() == "am" and hours == 12:
        hours = 0
    return f"{hours:02}:{minutes:02}"




if __name__ == "__main__":
    main()
