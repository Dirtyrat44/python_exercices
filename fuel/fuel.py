def main():
    user_input = input("Fraction: ")

    print(fuel_gauge(user_input), "%", sep="")



def fuel_gauge(t):
    try:
        n1, n2 = t.split("/")
    except:
        return
    else:
        n1, n2 = t.split("/")
    n1 = convert_int(n1)
    n2 = convert_int(n2)
    while True:
        try:
            n1 / n2
        except ZeroDivisionError:
            print("You cannot divide by zero")
            break
        else:
            return ((n1 / n2) * 100)

def convert_int(n):
    while True:
        try:
            n = int(n)
        except ValueError:
            print(f"'{n}' is not an intenger")
            break
        else:
            return n



main()
