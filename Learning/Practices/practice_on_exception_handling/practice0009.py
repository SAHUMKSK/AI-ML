# 9. Use else to print the result only when there is no exception.

try:
    dividend = int(input("Enter the number you want to divide: "))
    divisor = int(input("Enter the number you want to divide by: "))

    result = dividend / divisor
except ZeroDivisionError:
    print("You can not divide any number by 0.")
except ValueError:
    print("Only numbers are allowed.")
else:
    print(result)