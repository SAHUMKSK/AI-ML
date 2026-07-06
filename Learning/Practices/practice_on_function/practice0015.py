# 1. Write a program with a local variable score inside a function and a global one outside.
'''
a = 50 # This is global variable

def number():
    a = 10 # This is local variable.
    print("Local variable:", a)

number()
print("Global variable:", a)
'''
# 2. Create a program using global keyword to modify a variable from inside a function.
print()
b = 100

def globalFunc():
    global b # Here we converted to global.
    b = 200
    print("Inside the function:", b)


print("Before function call:", b)
globalFunc()
print("After function call:", b)

# 3. Explain the difference between local and global scope in your own words.
'''
1. We can define the local variables inside a function whereas we can define the global variables otside the function.

2. Local variables can not be accessible outside the function whereas global variables can be accessible outside the function.

'''