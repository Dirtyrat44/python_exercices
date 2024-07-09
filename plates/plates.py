def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) >= 2 and len(s) <= 6:
        if s[0, 2].isalpha():
            if s[-1].isdigit():
                 return True
            else:
                 return False

        else:
            return False
    else:
            return False


main()
