
# Script to check if a number is Armstrong or not

num = int(input("Enter a number: "))
sum = sum(int(digit)**len(str(num)) 
          for digit in str(num))
if num == sum:
    print(f"{num} is Armstrong")
else:
    print(f"{num} is not Armstrong")