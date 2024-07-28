import sys


def main():
    ...






def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3 and os.path.splitext(sys.argv[1]) != os.path.splitext(sys.argv[2]):
        sys.exit("")

if __name__ == "__main__":
    main()
