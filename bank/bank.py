def main():
    message = intput("Greeting: ")
    print(f"${money(message)})


def money(text):
    word = text.replace(",", " ").split(" ", 1).lower()
    if word == "hello":
        return "0"
    elif word



main()
