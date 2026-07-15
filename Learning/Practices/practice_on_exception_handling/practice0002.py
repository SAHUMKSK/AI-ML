# Handle ZeroDivisionError.

try:
    dividend = int(input("Enter the number you want to divide: "))
    divisor = int(input("Enter the number you want to divide by: "))

    result = dividend / divisor
except ZeroDivisionError:
    print("You can not divide any number by 0.")
except:
    print("Something went wrong.")
else:
    print(result)