# Find the sum of digits of a number.

number = int(input("Enter the number: "))

if number < 0:
    print("You entered the negative number.")
else:
    string = str(number)
    sum = 0
    for i in range(len(string)):
        sum = sum + (int(string[i]))
    print("Sum of the digits is: ", sum)