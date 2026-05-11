# --- Tests for lazy to_roman_lazy ---

import lazy_roman_numerals

def test_lazy_4():
    # Lazy style: IIII
    assert lazy_roman_numerals.to_roman_lazy(4) == "IIII"

def test_lazy_9():
    # Lazy style: VIIII
    assert lazy_roman_numerals.to_roman_lazy(9) == "VIIII"

def test_lazy_150():
    # 150 in lazy = C + L (100 + 50)
    assert lazy_roman_numerals.to_roman_lazy(150) == "CL"

def test_lazy_1000():
    assert lazy_roman_numerals.to_roman_lazy(1000) == "M"

def test_lazy_2000():
    # Just two Ms
    assert lazy_roman_numerals.to_roman_lazy(2000) == "MM"


# --- Optional: edge / negative cases (if you want to be strict)
# (Adjust behavior in your function if you don't want to support 0 or negatives.)

def test_roman_zero():
    # Decide what behaviour you want for 0.
    # For example, empty string:
    assert lazy_roman_numerals.to_roman_lazy(0) == ""

def test_lazy_zero():
    assert lazy_roman_numerals.to_roman_lazy(0) == ""