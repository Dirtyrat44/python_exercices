import pytest
from numb3rs import validate, check_number

def main():
    test_validate()
    test_check_number()
    test_check_number_alpha()
def test_validate():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1") == False
    assert validate("1.1") == False
    assert validate("1") == False

def test_check_number():
    assert check_number("1") == True
    assert check_number("255") == True
    assert check_number("256") == False
    assert check_number("-1") == False

def test_check_number_alpha():
    assert check_number("cat") == False



if __name__ == "__main__":
    main()
