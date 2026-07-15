# 10. Use finally to print "Thank you for using the program" regardless of whether an error occurs.

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
finally:
    print("Thank you for using the program.")