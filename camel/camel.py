def main():
    user_input = input("camelCase: ")
    print(camelCase(user_input))

def camelCase(t):
    for s in range(len(t)):
        if s.isupper():
            s = t[s].upper()
            t[s].insert([s - 1], " ")

    return t




main()
