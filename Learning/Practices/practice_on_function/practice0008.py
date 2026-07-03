# Create a function that prints all numbers from 1 to n.

def print_natural_numbers(numbers):
    for i in range(1, numbers + 1):
        print(i)

print_natural_numbers(int(input("Enter the number you want to print alll the natural numbers: ")))