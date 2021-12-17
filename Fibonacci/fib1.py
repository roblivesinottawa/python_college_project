def fibonacci(n):
    """
    Calculate the nth Fibonacci number
    """
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
print(fibonacci(20))
print(fibonacci(30))