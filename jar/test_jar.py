from jar import Jar
import pytest


def test_init():
    jar = Jar(15)
    assert jar.capacity == 15
    assert jar.size == 0



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(50)


def test_withdraw():
    jar = Jar(10, 10)
    jar.withdraw(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(20)
