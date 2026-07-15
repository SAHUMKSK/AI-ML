# 1. Divide two numbers using try and except.

try:

    dividend = int(input("Enter the number you want to divide: "))
    divisor = int(input("Enter the number you want to divide by: "))

    result = dividend / divisor

except:

    print("Something went wrong.")

else:

    print(result)