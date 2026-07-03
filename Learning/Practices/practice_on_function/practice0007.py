# Create a function that takes three numbers and prints the largest.


def largest_of_numbers(a, b, c):
    if a >= b and a >= c:
        print(f"The largest number is {a}")
    elif b >= a and b >= c:
        print(f"The largest number is {b}")
    else:
        print(f"The largest number is {c}")


largest_of_numbers(int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")), int(input("Enter the 3rd number: ")))