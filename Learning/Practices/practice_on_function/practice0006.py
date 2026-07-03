# Create a function that checks whether a number is even or odd.

def check_odd_or_even(number):
    if number % 2 == 0:
        print("Given number is even.")
    else:
        print("Given number is odd.")

check_odd_or_even(int(input("Enter the  number you want to check whether it is odd or even: ")))