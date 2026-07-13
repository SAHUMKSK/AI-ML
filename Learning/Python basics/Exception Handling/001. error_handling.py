'''
Exception:
An exception is an event, which occurs during execution of a program that disrupts the normal flow of the program's instructions.
An exception is a python object that represents an error.

Exception Handling: When an error occurs, or exception as we call it.

number = int(input("Enter your number: "))

result = number / 10

print(number / 0)
'''

try:
    number = int(input("Enter your number you want to divide by: "))

    result = 100 / number

    print(result)
except:
    print("Something went wrong.")