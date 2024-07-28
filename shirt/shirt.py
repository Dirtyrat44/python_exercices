import sys
import os


def main(): ...


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3 and os.path.splitext(sys.argv[1]) != os.path.splitext(
        sys.argv[2]
    ):
        sys.exit("Input and output have different extensions")
    elif (
        len(sys.argv) == 3
        and not sys.argv[1].endswith(".jpg", ".jpeg", ".png").lower()
        and not sys.argv[2].endswith(".jpg", ".jpeg", ".png").lower()
    ):
        sys.exit("Invalid input")

    if (
        len(sys.argv) == 3
        and sys.argv[1].endswith(".jpg", ".jpeg", ".png").lower()
        and sys.argv[2].endswith(".jpg", ".jpeg", ".png").lower()
        and os.path.splitext(sys.argv[1]) == os.path.splitext(sys.argv[2])
    ):
        return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    main()
