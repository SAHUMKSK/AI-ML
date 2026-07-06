# 9. Check whether a number is a palindrome.

number = int(input("Enter the number to check if it is a palindrome: "))
'''
if number < 0:
    print("You entered negative number.")

else:
    string = str(number)

    reversed_string = string[::-1]

    if string == reversed_string:
        print("Given number is palindrome.")
    else:
        print("Given number is not palindrome.")
'''

string = str(number)

if number >= 0 and string == string[::-1]:
    print("Given number is palindrome.")
else:
    print("Given number is not palindrome.")