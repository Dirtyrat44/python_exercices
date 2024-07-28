import csv
import sys


def main():
    argument_1, argument_2 = check_arguments()
    with open(argument_1) as before, open(argument_2, "w") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])




def check_arguments():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 3 and not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    if len(sys.argv) == 3 and sys.argv[1].endswith(".csv"):
        return sys.argv[1] and sys.argv[2]

if __name__ == "__main__":
    main()
