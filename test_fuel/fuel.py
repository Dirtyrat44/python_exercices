def main():
    while True:
        user_input = input("Fraction: ")
        if user_input.replace("/", "").isdigit() and "/" in user_input:
            try:
                percentage = convert(user_input)
                if percentage is not None:
                    print(gauge(percentage))
                    break
            except ValueError:
                break


def convert(s):
    numerator, denominator = map(int, s.split("/"))
    if numerator > denominator:
        return None
    else:
        try:
            return round((numerator / denominator) * 100)
        except ZeroDivisionError:
            return None



def gauge(n):
    if n in [99, 100]:
        return "F"
    elif n in [0, 1]:
        return "E"
    else:
        return f"{n}%"

main()
