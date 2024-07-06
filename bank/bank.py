def main():
    message = input("Greeting: ")
    print(f"${money(message)}")


def money(text):
    word = text.replace(",", " ").split(" ", 1).lower()
    if word == "hello":
        return "0"
    elif word.startswith("h"):
        return "20"
    else:
        return "100"



main()
