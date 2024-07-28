import sys


def main():
    print(check_argument())





def check_argument():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 2 and not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    if len(sys.argv) == 2 and sys.argv[1].endswith(".csv"):
        return sys.argv[1]

if __name__ == "__main__":
    main()
