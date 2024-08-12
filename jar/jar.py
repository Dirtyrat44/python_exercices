import sys

class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

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
        if self.size == 0:
            return "There is no cookies in the jar"
        elif self.size > 0 and self.size <= self.capacity:
            return f"there are {self._size}"

    @size.setter
    def size(self, size=0):
        self._size = 0

def main():
    try:
        user = int(input("What's the capacity of your cookie jar? "))
    except ValueError:
        sys.exit("Must be an Intenger")
    jar = Jar(user)
    print(jar.capacity)
    print(jar)
    print(jar.size)

if __name__ == "__main__":
    main()
