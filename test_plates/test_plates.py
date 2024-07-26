from plates import is_valid

def test_plates():
    assert is_valid("CS50") == True

def test_plates_non_alphabetical():
    assert is_valid("00") == False

def test_plates_lenght():
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("CSSSS50") == False

def test_plates_number_placement():
    assert is_valid("CS50S") == False

def test_plates_0_placement():
    assert is_valid("CS05") == False




