# Check whether a number is a perfect number.

number = int(input("Enter the number to check whether the number is perfect or not: "))

if number < 0:
    print("You entered the negative number.")
else:
    
    divisior = []
    
    total = 0
    
    for i in range(1, number):
        if number % i == 0:
            divisior.append(i)
    
    total = sum(divisior)
    
    if total == number:
        print("This is a perfect number.")
    else:
        print("This is not a perfect number.")