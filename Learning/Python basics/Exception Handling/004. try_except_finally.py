# try except finally: Finally block always execute.

try:
    dividend = int(input("Enter the number you want to divide: "))
    divisor = int(input("Enter the number you want to divide by: "))

    result = dividend / divisor

except ZeroDivisionError:
    print("You can not eneter 0 as divisior.")
    print("Always it will be 0.")
except ValueError:
    print("Only numbers are allowed.")

else:
    print(result)

finally:
    print("Program finished.")