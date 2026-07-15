# 4. Ask for age and handle invalid input.

try:
    age = int(input("Enter your age: "))

except ValueError:
    print("Please enter numbers only.")
except:
    print("Something went wrong.")
else:
    print(f"Your age is {age}.")