def main():
    user_input = input = ("Fraction: ")

    print(fuel_gauge(user_input, "%", sep=""))



def fuel_gauge(t):
    n1, n2 = t.split("/", 1)
    convert_int(n1)
    convert_int(n2)
    return ((n1 / n2) * 100)

def convert_int(n):
    try:
        float(n)



main()
