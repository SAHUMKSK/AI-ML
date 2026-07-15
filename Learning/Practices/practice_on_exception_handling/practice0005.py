# 5. Convert user input to an integer safely.

try:
    numberAsString = input("Enter the number: ")

    convertedNumber = int(numberAsString)

except ValueError:
    print("Only numbers are allowed.")

else:
    print(f"You entered {convertedNumber}")