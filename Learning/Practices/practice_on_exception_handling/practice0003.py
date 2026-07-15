# 3. Handle ValueError when the user enters text instead of a number.

try:

    dividend = int(input("Enter the number you want to divide: "))
    divisor = int(input("Enter the number you want to divide by: "))

    result = dividend / divisor
except ValueError:
    print("Only numbers are allowed.")
except:
    print("Something went wrong.")
else:
    print(result)