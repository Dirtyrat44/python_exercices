class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity


    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity=12):
        if not capacity >= 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        ...

def main():
    jar = Jar()


if __name__ == "__main__":
    main()

def main():
    jar = Jar()
    print(jar)

if __name__ == "__main__":
    main()
