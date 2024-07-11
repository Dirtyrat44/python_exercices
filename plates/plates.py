def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() and 1 < len(s) < 7 and all(c not in [" ", ",", ".", "'"] for c in s):
        is_digit = False
        for i, c in enumerate(s):

            if c.isdigit():
                is_digit = True
                if c == "0" or not s[i:].isdigit():
                   return False
                break

        if not is_digit:
            return True

        return is_digit
    else:
        return False









main()
