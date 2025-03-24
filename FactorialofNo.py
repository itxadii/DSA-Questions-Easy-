# 5️⃣ Find the Factorial of a Number
# Compute the factorial of a given number using recursion.

def factorial(n):
    if n == 1 or n == 0:
        return n
    return n * factorial(n-1)

print(factorial(5))
