import sys

def main():
    print(is_argv_ok())



def is_argv_ok():
    if len(sys.argv) == 1:
        sys.exit("Too few command-lines argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        return True

if __name__ == "__main__":
    main()
