def main():
    user_input = input("camelCase: ")
    print(camel_to_case(user_input))


def camel_to_case(text):
    new_str = []
    for char in text:
        if char.isupper():
            new_str.append("_")
            new_str.append(char.lower())
        else:
            new_str.append(char)

    return "".join(new_str)



main()
