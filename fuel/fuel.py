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
                    break
                elif percentage == 1 or 0:
                    print("E")
                    break
                else:
                    print(f"{percentage}%")
                    break




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



