# Multiply except block: Specific to error.

try:
    number = int(input("Enter your number: "))

    result = number / 0

    print(result)
except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("You can not eneter 0.")
except:
    print("Something went wrong.")