def main():
    message = input("Greeting: ")
    print(f"${money(message)}")


def money(text):
    text.lower().replace(",", " ")
    word = text.split(" ", 1)[0]
    if word == "hello":
        return "0"
    elif word.startswith("h"):
        return "20"
    else:
        return "100"



main()
