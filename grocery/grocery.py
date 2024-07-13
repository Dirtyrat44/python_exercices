grocery = {}

def main():
    while True:
        try:
            user_input = input("").upper()
            new_entry = {user_input: 1}
            grocery.update(new_entry)

        except EOFError:
            sorted_grocery = sorted(grocery)
            for items in sorted_grocery:
                print(sorted_grocery[items], items)
            break







main()
