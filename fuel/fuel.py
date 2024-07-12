def main():
    user_input = input("Fraction: ")

    print(fuel_gauge(user_input), "%", SEP="")



def fuel_gauge(t):
    n1, n2 = t.split("/", 1)
    n1 = convert_int(n1)
    n2 = convert_int(n2)
    while True:
        try:
            n1 / n2
        except ZeroDivisionError:
            print("You cannot divide by zero")
        else:
            return ((n1 / n2) * 100)

def convert_int(n):
    while True:
        try:
            int(n)
        except ValueError:
            print(f"'{n}' is not an intenger")
        else:
            return int(n)



main()
