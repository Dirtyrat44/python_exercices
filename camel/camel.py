def main():
    user_input = input("camelCase: ")
    print(camelCase(user_input))

def camelCase(t):
    text = []
    for s in range(len(t)):
        if t[s].isupper():
            text.append(t[s].lower())
            text[s].insert(text[s - 1], " ")
        else:
            text.append(t[s])

    return text




main()
