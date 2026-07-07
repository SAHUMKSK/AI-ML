# 33. Create a list of squares of even numbers from 1 to 20.

squareOfEvenNumbers = []

for i in range(21):
    if i % 2 == 0:
        squareOfEvenNumbers.append(i * i)

print(squareOfEvenNumbers)