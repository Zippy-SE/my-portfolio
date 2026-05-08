#The Fibonacci sequence is a number pattern where each term is the sum of the two numbers before it. 
#It usually starts like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ....



def find_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    curr = 1

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr

print(find_fibonacci(3))  # 2
print(find_fibonacci(7))  # 13