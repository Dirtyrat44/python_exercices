import pytest
from numb3rs import validate



def test_ip_format():
    assert validate(r"0.0.0.0") == True
    assert validate(r"0") == False
    assert validate(r"0.0") == False
    assert validate(r"0.0.0") == False

def test_ip_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.1.1.1") == False
    assert validate(r"1.512.1.1") == False
    assert validate(r"1.1.1.512") == False
    assert validate(r"1.1.512.1") == False
