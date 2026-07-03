# Find the largest of three numbers.

print("Enter all the three number to check the largest number:")

number1 = int(input("1st number: "))
number2 = int(input("2nd number: "))
number3 = int(input("3rd number: "))

if number2 < number1 > number3:
    print("1st number is largest.")
elif number1 < number2 > number3:
    print("2nd number is largest.")
else:
    print("3rd number is largest.")