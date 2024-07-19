import inflect
p = inflect.engine()
def main():
    names = []
    while True:
        try:
            user_input = input("Name: ")
            names.append(user_input)
        except EOFError:
            print()
            print(f"Adieu, adieu, to {p.join(names)}")
            break












if __name__ == "__main__":
    main()
