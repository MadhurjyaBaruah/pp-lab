

# Script to generate prime numbers series up to n
n = int(input("Enter limit: "))
primes = []

for num in range(2, n + 1):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
    if count == 0:
        primes.append(num)

print("Prime numbers are:", primes)
