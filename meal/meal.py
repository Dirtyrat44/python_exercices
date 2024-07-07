def main():
    user_input = input("What time is it? ")
    time = convert(user_input)
    hours, minutes = map(float, time.split("."))
    
    if hours == 7:
        print("breakfast time")
    elif hours == 8 and minutes == 0:
        print("breakfast time")
    elif hours == 12:
        print("lunch time")
    elif hours == 13 and minutes == 0:
        print("lunch time")
    elif hours == 18:
        print("dinner time")
    elif hours == 19 and minutes == 0:
        print("dinner time")
    else:
        return


def convert(time):
    hours, minutes = time.split(":")
    minutes = round(float(minutes) / 60, 2)
    hours = int(hours)
    return f"{hours + minutes:.1f}" if minutes == 0 else f"{hours + minutes:.2f}".rstrip("0").rstrip(".")





if __name__ == "__main__":
    main()
