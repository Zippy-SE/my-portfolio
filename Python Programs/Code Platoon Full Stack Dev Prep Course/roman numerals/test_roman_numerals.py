import roman_numerals


# --- Tests for modern to_roman ---

def test_roman_4():
    assert roman_numerals.to_roman(4) == "IV"

def test_roman_9():
    assert roman_numerals.to_roman(9) == "IX"

def test_roman_14():
    assert roman_numerals.to_roman(14) == "XIV"

def test_roman_44():
    assert roman_numerals.to_roman(44) == "XLIV"

def test_roman_944():
    assert roman_numerals.to_roman(944) == "CMXLIV"

def test_roman_150():
    assert roman_numerals.to_roman(150) == "CL"

def test_roman_1000():
    assert roman_numerals.to_roman(1000) == "M"

def test_roman_edge_1():
    assert roman_numerals.to_roman(1) == "I"

def test_roman_large_enough():
    # 3500 just appends more M's
    assert roman_numerals.to_roman(3500) == "MMMD"