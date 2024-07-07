def main():
    user_input = input("camelCase: ")
    print(camelCase(user_input).replace(" ", "_"))

def camelCase(t):
    text = []
    for s in range(len(t)):
        if t[s].isupper():
            text.append(" ")
            text.append(t[s].lower())

        else:
            text.append(t[s])

    return "".join(text)




main()
