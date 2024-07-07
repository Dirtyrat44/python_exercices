def main():
    user_input = input("camelCase: ")
    print(camelCase(user_input))

def camelCase(t):
    text = []
    for s in range(len(t)):
        if t[s].isupper():
            text = t[s].upper()
            text[s].insert([s - 1], " ")
        else:
            text = t[s]

    return text




main()
