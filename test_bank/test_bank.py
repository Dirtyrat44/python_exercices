from bank import value

def test_value_0():
    assert value("Hello") == "0"
    assert value("hello") == "0"
    assert value("hello, my name is arthur") == "0"

def test_value_20():
    assert value("How are you ?") == "20"
    assert value("Hi") == "20"

def test_value_100():
    assert value("Arthur") == "100"
    assert value("What ?") == "100"
