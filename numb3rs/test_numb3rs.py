import pytest
from numb3rs import validate, check_number

def test_validate():
    assert validate("1.1.1.1") == "True"

def test_check_number():
    assert check_number("1") == True

def test_check_number_alpha():
    with pytest.raises(ValueError):
        check_number("cat")
