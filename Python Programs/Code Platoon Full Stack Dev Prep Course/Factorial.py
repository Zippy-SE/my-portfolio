def factorial(n):
    # Edge case: 0! is 1
    if n == 0:
        return 1
    
    result = 1
    # Loop from n down to 1
    for i in range(1, n + 1):
        result *= i
    return result

# Testing the function
print(factorial(4)) # Output: 24