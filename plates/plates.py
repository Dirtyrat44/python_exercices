def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if range(s) >= 2 and range(s) <= 6:
        if s[0, 2].isalpha():
            

        else:
            return False
    else:
            return False


main()
