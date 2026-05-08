import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    calculator.calculate(10, 2, "multiply")
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

# Add more tests to cover edge cases and negative scenarios, such as dividing by zero or invalid operations.

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_subtract():
    assert calculator.calculate(5, 3, "subtract") == 2

def test_multiply():
    assert calculator.calculate(4, 3, "multiply") == 12

def test_divide():
    assert calculator.calculate(10, 2, "divide") == 5.0

# Test terminal output (stdout) for different operations
def test_terminal_output_add(capsys):
    calculator.calculate(2, 3, "add")
    captured = capsys.readouterr()
    assert captured.out == "Result: 5\n"

def test_terminal_output_subtract(capsys):
    calculator.calculate(5, 3, "subtract")
    captured = capsys.readouterr()
    assert captured.out == "Result: 2\n"

def test_terminal_output_multiply(capsys):
    calculator.calculate(4, 3, "multiply")
    captured = capsys.readouterr()
    assert captured.out == "Result: 12\n"

def test_terminal_output_divide(capsys):
    calculator.calculate(10, 2, "divide")
    captured = capsys.readouterr()
    assert captured.out == "Result: 5.0\n"

# Test divide by zero (error case)
def test_divide_by_zero():
    try:
        calculator.calculate(10, 0, "divide")
        assert False, "Expected ValueError for divide by zero"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

# Test invalid operation (unsupported operation)
def test_invalid_operation():
    # You can define what your calculator should do here;
    # the current code does not handle this, so it will return 0.
    result = calculator.calculate(5, 3, "unknown")
    assert result == 0  # or you can change the behavior if you like

# Test negative numbers
def test_negative_numbers():
    assert calculator.calculate(-2, 3, "add") == 1
    assert calculator.calculate(2, -3, "subtract") == 5
    assert calculator.calculate(-2, -3, "multiply") == 6

# Test floating point numbers
def test_float_numbers():
    assert calculator.calculate(5.5, 4.5, "add") == 10.0

# Test that the printed output is consistent (no extra spaces or lines)
def test_output_formatting(capsys):
    calculator.calculate(0, 0, "add")
    captured = capsys.readouterr()
    assert captured.out == "Result: 0\n"

# Test that the function returns the correct result for 0
def test_zero_result():
    assert calculator.calculate(0, 5, "subtract") == -5

# Test that the function works correctly with the same number
def test_same_numbers():
    assert calculator.calculate(3, 3, "add") == 6
    assert calculator.calculate(3, 3, "subtract") == 0
    assert calculator.calculate(3, 3, "multiply") == 9
    assert calculator.calculate(3, 3, "divide") == 1.0

