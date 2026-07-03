# 8. Reverse a number.

number = int(input("Enter the number you want to reverse : "))

if number < 0:
    is_negative = True
else:
    is_negative = False

string = str(abs(number))

reversed_string = string[::-1]

if is_negative == True:
    print("-", reversed_string, sep = "")
else:
    print(reversed_string)

