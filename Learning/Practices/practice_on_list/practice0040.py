# 40. Create a list containing only odd numbers from 1 to 50.

oddNumbers = []

for i in range(51):
    if i % 2 != 0:
        oddNumbers.append(i)

print(oddNumbers)