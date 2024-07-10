def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Check if first 2 are alpha, if min len is 2 and max len is 6 and if s doesn't contain ponctuation
    if s[0:2].isalpha() and 6 >= len(s) > 1 and all (c not in [" ", "'", "."] for c in s):
        digit_seen = False
        for i, c in enumerate(s):
            if c.isdigit():
                digit_seen = True
                if c == "0" or not s[i:].isdigit():
                    return False
            break
        if not digit_seen:
            return True
        else:
            return False



    else:
        return False





main()


