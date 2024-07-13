grocery = {}

def main():
    while True:
        try:
            user_input = input("").upper()
            new_entry = {user_input: 1}
            grocery.update(new_entry)

        except EOFError:
            sorted_grocery = sorted(grocery)
            for key in sorted_grocery:
                value = sorted_grocery[key]
                print(f"{value} {key}")
            break







main()
