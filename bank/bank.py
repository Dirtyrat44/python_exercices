def main():
    message = input("Greeting: ")
    print(f"${money(message)}")


def money(text):
    word = text.lower().replace(",", " ").split(" ", 1)
    if word == "hello":
        return "0"
    elif word.startswith("h"):
        return "20"
    else:
        return "100"



main()
