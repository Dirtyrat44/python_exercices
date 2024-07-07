def main():
    user_input = input("camelCase: ")
    output = camelCase(user_input)
    for text in output:
        print(text, sep="", end="")
        print()

def camelCase(t):
    text = []
    for s in range(len(t)):
        if t[s].isupper():
            text.append(" ")
            text.append(t[s].lower())

        else:
            text.append(t[s])

    return text




main()
