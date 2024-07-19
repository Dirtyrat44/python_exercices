import random


def main():
    level = get_level()


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2 ,3]:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    upper_bound = (10**level) - 1
    lower_bound = 10**(level - 1)
    return random.randint(lower_bound, upper_bound)


if __name__ == "__main__":
    main()
