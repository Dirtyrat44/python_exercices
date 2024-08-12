class Jar:
    def __init__(self, capacity=12):
        if not capacity >= 0:
            raise ValueError("Invalid capacity")
        self.capacity = capacity


    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

def main():
    jar = Jar(15)
    print(jar)

if __name__ == "__main__":
    main()
