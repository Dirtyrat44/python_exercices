grocery = {}

def main():
    while True:
        try:
            user_input = input("").upper()
            new_entry = {user_input: 1}
            grocery.update(new_entry)

        except EOFError:
            sorted_grocery = sorted(grocery)
            for item, quantity in sorted_grocery.items():
                print(quantity, item, end=" ")
            break







main()
