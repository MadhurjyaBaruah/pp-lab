
#Script to print sum of N natural numbers
n = int(input("Enter a limit N: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print(f"Sum: {total}")