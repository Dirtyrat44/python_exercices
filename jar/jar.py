import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return f"Cookie monster"

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return f"The jar capacity is : {self._capacity}"

    @capacity.setter
    def capacity(self, capacity=12):
        if not capacity >= 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        ...

def main():
    try:
        user = int(input("?: "))
    except ValueError:
        sys.exit("Must be an Intenger")
    jar = Jar(user)
    print(jar.capacity)
    print(jar)

if __name__ == "__main__":
    main()
