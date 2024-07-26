def main():
    user_input = input("Fraction: ")
    converted_fraction = convert(user_input)
    output = gauge(converted_fraction)
    print(output)


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
