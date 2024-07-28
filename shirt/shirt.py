import sys
import os
import PIL

def main():
    input_file, outpufile = check_arguments()
    with PIL.Image.open()


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file, output_file = sys.argv[1], sys.argv[2]
    valid_extensions = (".jpg", ".jpeg", ".png")

    if (
        os.path.splitext(input_file)[1].lower()
        != os.path.splitext(output_file)[1].lower()
    ):
        sys.exit("Input and output have different extensions")

    if not (
        input_file.lower().endswith(valid_extensions)
        and output_file.lower().endswith(valid_extensions)
    ):
        sys.exit("Invalid input")

    return input_file, output_file


if __name__ == "__main__":
    main()
