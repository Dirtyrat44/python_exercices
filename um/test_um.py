import pytest
from um import count

def test_count_case_insensitive():
    assert count(r"Um HellO WorlD UM,") == 2
    assert count(r"HellO WorlD UMbRella,") == 0

def test_count_spaces():

    assert count(r" um um um") == 3
    assert count(r"umum") == 0



