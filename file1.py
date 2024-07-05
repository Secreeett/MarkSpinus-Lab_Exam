def factorial(n):
    if n == 0:
        return 1
    else:
        result = n * factorial(n-)
        print(f"factorial({n}) = {result}")
        return = result

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

result = factorial(5)
print(f"Factorial of 5 is: {result}")

result = fibonacci_sequence(10)
print(f"Fibonacci sequence up to 10 numbers:")
