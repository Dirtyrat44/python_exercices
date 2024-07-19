import random

def main():

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass

        if level > 0:
            guess_number = random.randint(1, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                except ValueError:
                    pass
                if guess > 0:
                    print(is_guess_true(level, guess))

                else:
                    pass




def is_guess_true(n_to_find, n):
    if n > n_to_find:
        return "Too large!"
    elif n < n_to_find:
        return "Too small!"
    else:
        return "Just right!"

if __name__ == "__main__":
    main()
