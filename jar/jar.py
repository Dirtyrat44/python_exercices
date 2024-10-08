import sys


class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def deposit(self, n):

        if self.size + n > self.capacity:
            raise ValueError("Can't add that many cookies")
        self.size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("There isnt enough cookies to withdraw")
        self.size -= n

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

    def __str__(self):
        return f"{'🍪' * self.size}"


def main():
    jar = Jar(15)
    print(jar)
    jar.size = 5
    print(jar)
    jar.deposit(2)
    print(jar)
    jar.withdraw(5)
    print(jar)


if __name__ == "__main__":
    main()
