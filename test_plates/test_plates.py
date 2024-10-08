from plates import is_valid
import pytest

def test_plates():
    assert is_valid("CS50") == True

def test_plates_non_alphabetical():
    assert is_valid("1AAA") == False
    assert is_valid("A1AA") == False
    assert is_valid("AA50") == True
    assert is_valid("50") == False

def test_plates_length():
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("CSSSS50") == False

def test_plates_number_placement():
    assert is_valid("CS50S") == False

def test_plates_0_placement():
    assert is_valid("CS05") == False

def test_plates_alphanumeric():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS,50") == False
    assert is_valid("CS.50") == False
    assert is_valid("CS'50") == False
