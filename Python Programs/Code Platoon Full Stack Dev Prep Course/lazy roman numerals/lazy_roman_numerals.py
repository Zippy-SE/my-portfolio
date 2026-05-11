def to_roman_lazy(num):
    value_to_roman = [
        (1000, "M"),
        (500,  "D"),
        (100,  "C"),
        (50,   "L"),
        (10,   "X"),
        (5,    "V"),
        (1,    "I")
    ]

    result = ""

    for value, roman in value_to_roman:
        count = num // value
        result += roman * count
        num -= value * count

    return result

print(to_roman_lazy(4))    # "IIII"
print(to_roman_lazy(944))  # "DCCCCLXXXXIIII"
print(to_roman_lazy(150))  # "CCCL"
