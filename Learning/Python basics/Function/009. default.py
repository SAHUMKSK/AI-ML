# Default & Keyword Arguments: A Default value is set during function definition so that in a function call if the argument iis not provided then the interpreter will use that predefined value as an argument.

# If no arguments is provided default values will be used.

def greet(name = "Sir"):
    print(f"Hello {name}, Welcome!")

greet("Mukesh") # Here we passed the arguments so it override the parameters.
greet() # Here we have not passed any of the arguments sdo it consider the default arguments.
    