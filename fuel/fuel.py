def main():
    while True:
        user_input = input("Fraction: ")
        if user_input.isalpha():
            pass
        else:
            try:
                convert_and_return(user_input)
            except:
                pass
            else:
                print()




def convert_and_return(str):
    while True:
        try:
            n1, n2 = str.split("/")
        except:
            break
        else:
            n1 = convert_int(n1)
            n2 = convert_int(n2)
            break











main()





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




