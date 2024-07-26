def main():
    user_input = input("Fraction: ")
    converted_fraction = convert(user_input)
    output = gauge(converted_fraction)
    print(output)


def convert(s):
    while True:
        try:
            numerator, denominator = map(int, s.split("/"))
            f = numerator / denominator
            if f <= 1:
               return f * 100
            else:
                s = input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            s = input("Fraction: ")


def gauge(n):
    if n in [99, 100]:
        return "F"
    elif n in [0, 1]:
        return "E"
    else:
        return f"{n}%"

main()
