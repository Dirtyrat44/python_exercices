import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
figlet_available = figlet.getFonts()


def main():
    if len(sys.argv) == 1:
        s = input("Input: ")
        font_choice = choice(figlet_available)
        figlet.setFont(font=font_choice)
        print(f"Output: {figlet.renderText(s)}")

    elif (
        len(sys.argv) == 3
        and sys.argv[1] in ["-f", "--font"]
        and sys.argv[2] in figlet_available
    ):
        s = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(f"Output: {figlet.renderText(s)}")

    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
