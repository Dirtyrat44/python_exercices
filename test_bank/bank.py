def main():
    message = input("Greeting: ")
    print(f"${value(message)}")


def value(text):
    text = text.strip().lower().replace(",", " ")
    word = text.split(" ", 1)[0]
    if word == "hello":
        return "0"
    elif word.startswith("h"):
        return "20"
    else:
        return "100"


if __name__ == "__main__":
    main()
