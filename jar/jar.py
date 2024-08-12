import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return f"Your jar capacity is : {self.capacity} and there are : {size} cookies inside"

    def deposit(self, n):
        ...


    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity=12):
        if not capacity > 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar(15)
    print(jar)
    jar.size = 10
    print(jar)


if __name__ == "__main__":
    main()
