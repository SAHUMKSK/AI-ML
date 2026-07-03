# Create a function that prints the multiplication table of a given number.

def print_table(number):
    for i in range(1, 11):
        print(f"{number} X {i} = {number * i}")

print_table(int(input("Enter the mnumber you want to print the multiplication table: ")))