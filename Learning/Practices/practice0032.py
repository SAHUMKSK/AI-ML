# Find the product of digits of a number.

number = int(input("Enter the number you want product: "))

string = str(abs(number))

product = 1

for i in string:
    product = product * int(i)

print("product of the given number:", product)