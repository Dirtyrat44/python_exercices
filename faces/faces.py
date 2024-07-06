def main():
    input = input("How are you doing today ? ")
    print(convert(input))


def convert(message):
    return message.replace(":)", "🙂").replace(":(", "🙁")




main()
