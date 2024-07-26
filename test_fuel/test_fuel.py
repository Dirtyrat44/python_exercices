from fuel import convert, gauge


def test_correct_input():
    assert convert("1/4") == 25 and gauge(25) == "25%"
