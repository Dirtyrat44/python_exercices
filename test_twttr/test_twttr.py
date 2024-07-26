from twttr import shorten


def test_shorten_str():
    assert shorten("twitter") == "twttr"
    assert shorten("test") == "tst"

def test_shorten_int():
    assert shorten("5") == "5"
    assert shorten("0") == "0"
