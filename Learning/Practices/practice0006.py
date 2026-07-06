# 6. Find the factorial of a given number.

number = int(input("Enter the number you want factorial : "))

factorial = 1
if number < 0:
    print("You enetred the negative number.")
else:
    if number == 0:
        factorial = 1
    else:

        for i in range(number, 0, -1):
            factorial = factorial * i

print(f"Factorial of the {number} is", factorial)