def main():
    message = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    if is_correct(message.lower().strip()):
        print("Yes")
    else:
        print("No")

def is_correct(text):
    return text == "42" or text == "forty two" or text == "forty-two"


main()
