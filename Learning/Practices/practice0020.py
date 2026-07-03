# Calculate the sum of even numbers between 1 and N.

number = int(input("Enter the number you want to sum: "))

sum = 0

for i in range(1, number + 1):
    if i % 2 != 0:
        sum = sum + i
        
print(sum)