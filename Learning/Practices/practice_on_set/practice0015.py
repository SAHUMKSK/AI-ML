# Ask the user to enter five numbers and store only the unique numbers in a set, then print the final set.

numberSet = set()

for i in range(0, 5):
    numberSet.add(int(input("Enter the numbers you want to add: ")))

print(f"Unique values are: {numberSet}")