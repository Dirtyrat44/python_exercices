import pytest
from watch import parse


def test_watch():
    assert parse(r'src = "https://youtube.com/embed/xdDaedlol"') == "xdDaedlol"
