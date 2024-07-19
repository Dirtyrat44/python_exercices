import random


def main():
    level = get_level()


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2 ,3]:
                raise ValueError


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
