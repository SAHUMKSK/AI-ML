''' A function is a block of code that performs a specific task.

# Instead of writing the same code repeatedly, you write once and call it whenever you needed.

syntax:
def function_name():
    block of code

    
function_name()

'''


def greet():
    print("Hello")


greet()

print("2. Function with parameters")

def greet(name):
    print("Hello,", name, "Welcome!")

greet("Mukesh")

print("3. Function with multiple parameters")

def add(a, b):
    print( a + b )

add(10, 20)
