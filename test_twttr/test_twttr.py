from twttr import shorten

def test_shorten_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("test") == "tst"
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""

def test_shorten_non_vowels():
    assert shorten("bcdfg") == "bcdfg"
    assert shorten("BCDFG") == "BCDFG"

def test_shorten_punctuation():
    assert shorten("twttr!") == "twttr!"
    assert shorten("hello, world!") == "hll, wrld!"

def test_shorten_numbers():
    assert shorten("12345") == "12345"
    assert shorten("5") == "5"
    assert shorten("0") == "0"
