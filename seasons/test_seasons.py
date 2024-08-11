import pytest
from seasons import check_date_format
from datetime import date

def test_date_format():
    assert check_date_format("1993-1-8") == date(1993, 1, 8)
    assert check_date_format("2020-1-10") == date(2020, 1, 10)
    with pytest.raises(SystemExit):
        check_date_format("cat")
    with pytest.raises(SystemExit):
        check_date_format("1993-1")
