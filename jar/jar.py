import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        ...

    def deposit(self, n):
        self.n = n

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity=12):
        if not capacity > 0:
            raise ValueError("Invalid capacity")

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if self.size < 1 and self.size > self.capacity:
            raise ValueError("Your jar capacity can't contains this much cookies")
        self._size = size

