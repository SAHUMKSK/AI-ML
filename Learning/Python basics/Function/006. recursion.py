# Recursion: To call a same function inside the function.

# A recursive function is one that calls itself.
# It must have a base case (stopping condition) and a recursive case (repeats the function).
'''
def show(n):
    if n==0:
        return
    print(n)
    show(n - 1)
    print(n)
    
    for i in range(1,4):
    
        print(n)
    print("---------")

show(5)
'''
# Print the factorial of given number.

# number = int(input("Enter the number you want to print factorial: "))

fact = 1

def printFact(number):
    if (number == 0 or number == 1):
        return 1
    else:
        return number * printFact(number-1)

result = printFact(5)
print(result)