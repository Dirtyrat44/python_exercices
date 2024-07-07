def main():
    user_input = input("camelCase: ")
    print(camelCase(user_input))

def camelCase(t):
    for s in range(len(t)):
        text = t[s]
        if t[s].isupper():
            text = t[s].upper()
            t[s].insert([s - 1], " ")

    return text




main()
