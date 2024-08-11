import pytest
from seasons import check_date_format

def test_date_format():
    assert check_date_format("1993-1-8") == date(1993, 1, 8)
