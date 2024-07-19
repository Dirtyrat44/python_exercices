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
        


"""
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                guess_number = random.randint(1, level)
                while True:
                    try:
                        guess = int(input("Guess: "))
                    except ValueError:
                        pass
                    else:
                        if guess > 0:
                            if guess_number < guess:
                                print("Too large!")
                            elif guess_number > guess:
                                print("Too small!")
                            else:
                                print("Just right!")
                                return

                        else:
                            pass
"""






if __name__ == "__main__":
    main()
