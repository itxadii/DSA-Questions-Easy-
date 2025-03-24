# 2️⃣ Check if a Number is Prime
# Write a function to check whether a given number is prime.

num = 7 

def isPrime(num):
    if num < 2:
        return False 
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False 
    return True

print(isPrime(num))