import random

def main():

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
                            if guess_number > guess:
                                print("Too large!")
                            elif guess_number < guess:
                                print("Too small!")
                            else:
                                print("Just right!")
                                return

                        else:
                            pass




""" def is_guess_true(n_to_find, n):
    if n > n_to_find:
        return "Too large!"
    elif n < n_to_find:
        return "Too small!"
    else:
        return "Just right!"
"""

if __name__ == "__main__":
    main()
