def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not (1 < len(s) < 7 and s[0:2].isalpha()):
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
