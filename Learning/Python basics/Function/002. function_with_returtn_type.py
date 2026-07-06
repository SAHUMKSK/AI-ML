
# The return  statement is used to send a value back fromn a function.
# After return function stops the execution.
# While returning the values it can be anything.
# Explicitly specify user has to return the values.

def sumFunc(a = 10, b = 20):
    total = a + b
    return total

total = sumFunc()
print(f"Sum is {total}")

def subFunc(a = 20, b = 10):
    subtraction = a - b
    return subtraction

subtraction = subFunc()
print(f"Subtraction value is {subtraction}")

# A function can return multiple return values.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
role = input("Enter your role: ")

def printFunc(name, age, role):

    return name, age, role

name, age, role = printFunc(name, age, role)
print(type(name))
print(type(age))
print(type(role))

print(name)
print(age)
print(role)