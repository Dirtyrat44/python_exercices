def main():
    user_input = input("camelCase: ")
    print(camelCase(user_input))

def camelCase(t):
    for s in range(len(t)):
        if s.isupper():
            s = s.upper()
            s.insert([s - 1], " ")

    return t




main()
