grocery = {}

def main():
    while True:
        try:
            user_input = input("").upper()
            if user_input in grocery:
                grocery[user_input] += 1
            else:
                grocery[user_input] = 1


        except EOFError:
            sorted_grocery = sorted(grocery)
            for key in sorted_grocery:
                value = sorted_grocery[key]
                print(f"{value} {key}")
            break







main()
