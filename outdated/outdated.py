months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        user_input = input("Date: ")
        if user_input.replace("/", "").isdigit() and "/" in user_input:
            month, day, year = map(int, user_input.replace("/", " ").split(" "))
            if month < 13 and day < 32:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                pass
        elif "," in user_input:
            try:
                month, day, year = user_input.replace(",", "").split(" ")
                day = int(day)
                year = int(year)
            except ValueError:
                pass
            else:
                if month < 13 and day < 32:
                    if month in months:
                        #print month index +1
                        print(f"{year}-{months.index(month) + 1:02}-{day:02}")
                        break
                    else:
                        pass
                else:
                    pass


        else:
            pass









main()
