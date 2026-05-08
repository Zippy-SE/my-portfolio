def find_fibonacci(n):
    # Base cases: the first two numbers in the sequence
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    return find_fibonacci(n - 1) + find_fibonacci(n - 2)

# Test it
print(find_fibonacci(3))  # 2
print(find_fibonacci(7))  # 13