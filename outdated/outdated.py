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
            print(f"{year}-{month:02}-{day:02}")
            break
        elif user_input 









main()
