def main():
    user_input = input("Expression: ")
    print(maths(user_input))


def maths(string):
    x, y, z = string.split(" ")
    x, z = convert_to_int(x, z)

    match y:
        case "+":
          return f"{x + z:.1f}"
        case "-":
          return f"{x - z:.1f}"
        case "*":
          return f"{x * z:.1f}"
        case "/" if z != 0:
          return f"{x / z:.1f}"
        case _:
          return "Wrong operators"

def convert_to_int(n, n2):
   int_x = int(n)
   int_y = int(n2)
   return int_x, int_y


main()
