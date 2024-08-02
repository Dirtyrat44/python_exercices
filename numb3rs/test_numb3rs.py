import pytest
from numb3rs import validate



def test_ip_format():
    assert validate(r"0.0.0.0") == True
    assert validate(r"0") == False

def test_ip_range():
    assert validate(r"255.0.0.100") == True
