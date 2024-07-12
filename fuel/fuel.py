def main():
    while True:
        user_input = input("Fraction: ")
        if user_input.isalpha() and len(user_input) < 2:
            pass
        else:
            break














main()



def main():
    extract_fractions()

    print()







def extract_fractions():
    while True:
        try:
            user_input = input("Fraction: ")
            n1, n2 = user_input.split("/")
        except:
            return
        else:
            n1 = convert_int(n1)
            n2 = convert_int(n2)



def divide_return_percentage(n1, n2):
    while True:
            try:
                n1 / n2
            except ZeroDivisionError:
                print("You cannot divide by zero")

            else:
                return round((n1 / n2) * 100)

def convert_int(n):
    while True:
        try:
            n = int(n)
        except ValueError:
            print(f"'{n}' is not an intenger")
            break
        else:
            return n




