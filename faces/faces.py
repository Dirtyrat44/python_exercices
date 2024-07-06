def main():
    user_input = input("How are you doing today ? ")
    print(convert(user_input))


def convert(message):
    return message.replace(":)", "🙂").replace(":(", "🙁")




main()
