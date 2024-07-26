import sys


def main():

    if len(sys.argv) == 1 and sys.argv[1].endswith(".py"):
        try:
            command_argument = sys.argv[1]
        except FileNotFoundError:
            sys.exit("Not a Python file")
    else:
        sys.exit("Too few command-line arguments")












if __name__ == "__main__":
    main()
