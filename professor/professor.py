import random


def main():
    level = get_level()
    for _ in range(10):
        while True:
            n1, n2 = generate_integer(level), generate_integer(level)
            try:
                user_answer = int(input(f"{n1} + {n2} = "))
            except ValueError:
                pass
            else:



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
    if level == 1:
        return random.randint(0-9)
    else:
        upper_bound = (10**level) - 1
        lower_bound = 10**(level - 1)
        return random.randint(lower_bound, upper_bound)


if __name__ == "__main__":
    main()
