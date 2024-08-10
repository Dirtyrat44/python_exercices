import pytest
from working import convert

def test_convert_range():
    with pytest.raises(ValueError):
        convert(r"12:00 AM to 45:00 PM")
        convert(r"24:00 AM to 12:00 PM")
        convert(r"14 AM to 12 PM")
        convert(r"12 AM to 14 PM")

def test_convert_hours():
    assert convert(r"12 AM to 12 PM") == r"00:00 to 12:00"
    assert convert(r"11 AM to 11 PM") == r"11:00 to 23:00"
    assert convert(r"1 AM to 1 PM") == r"01:00 to 13:00"

def test_convert_ommit():
    with pytest.raises(ValueError):
        convert(r"12 AM 12 PM")
        convert(r"1:00 AM 5:30 PM")


