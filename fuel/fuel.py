def main():
    while True:
        user_input = input("Fraction: ")
        if user_input.isalpha():
            pass
        else:
            try:
                percentage = convert_and_return(user_input)
            except:
                pass
            else:
                if percentage == 100 or 99:
                    print("F")
                elif percentage == 1 or 0:
                    print("E")
                else:
                    print(f"{percentage}%")




def convert_and_return(str):
    while True:
        try:
            n1, n2 = str.split("/")
        except:
            return
        else:
            try:
                n1 = int(n1)
                n2 = int(n2)
            except ValueError:
                return
            else:
                pass


        try:
            n1 / n2
        except ZeroDivisionError:
            return
        else:
            return round((n1 / n2) * 100)













main()







def convert_int(n):
    while True:
        try:
            n = int(n)
        except ValueError:
            print(f"'{n}' is not an intenger")
            break
        else:
            return n




