from random import randint


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                return level


def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess > 0:
                return guess


def main():

    level = get_level()
    guess_number = randint(1, level)

    while True:
        guess = get_guess()

        if guess_number > guess:
            print("Too small!")
        elif guess_number < guess:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
