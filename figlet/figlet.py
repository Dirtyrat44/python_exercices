import sys
from pyfiglet import Figlet

figlet = Figlet()
figlet_available = figlet.getfonts()



def main():
    if len(sys.argv) == 0:
        sys.exit()


    elif len(sys.argv) == 2 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet_available:
            print()




    else:
        sys.exit("Invalid usage")



if __name__ == "__main__":
    main()
