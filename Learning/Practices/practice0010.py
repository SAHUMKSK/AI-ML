# 10. Print the multiplication table of any number.

number = int(input("Enter the number you want multiplication table: "))

if number < 0:
    print("you entered an invalid number.")
elif number == 0:
    print("Zero multiplication table is just zeros!")
else:
    for i in range(1, 11):
        print(number, " X ", i, " = ", number * i )