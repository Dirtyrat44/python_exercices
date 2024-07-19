import random

def main():

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass

        if level > 0:
            guess_number = random.randint(1, level)
            try:
                guess = int(input("Guess: "))
            except ValueError:
                pass
            if guess > 0:
                





if __name__ == "__main__":
    main()
