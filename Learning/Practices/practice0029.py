# Print all divisors of a number.

number = int(input("Enter the number: "))

divisiors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisiors.append(i)

print("Below are all the divisiors list.")
print(divisiors)