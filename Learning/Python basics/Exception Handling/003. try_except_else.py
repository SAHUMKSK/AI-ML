# try except else: Else block will execute when no exception occurs.

try:
    number = int(input("Enter the number you want to divide by: "))

    result = 100 / number

except ValueError:
    print("Only numbers are allowed.")
except ZeroDivisionError:
    print("You can not divide any number by 0.")
except:
    print("something went wrong.")
else:
    print(result)