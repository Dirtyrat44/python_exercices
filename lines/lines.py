import sys


def main():
    print(line_count(is_argv_ok()))


def is_argv_ok():
    if len(sys.argv) == 1:
        sys.exit("Too few command-lines argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
        return sys.argv[1]


def line_count(file_py):
    count = 0
    try:
        with open(file_py, "r") as file:
            for line in file:
                line = line.rstrip()
                if line and line not in [" ", "#"]:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    else:
        return count


if __name__ == "__main__":
    main()
