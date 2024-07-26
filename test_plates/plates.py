def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    if not s.isalnum():
        return False

    is_digit = False
    for i, c in enumerate(s):
        if c.isdigit():
            is_digit = True

            if c == "0" or not s[i:].isdigit():
                return False
            break

    if not is_digit:
        return True

    return True


if __name__ == "__main__":
    main()
