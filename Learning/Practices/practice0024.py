# Ask the user for a password. Give only 3 attempts using a loop.

password = input("Enter the password you want to keep: ")

for i in range(3):
    if password == input("Please Enter the password to access the system: "):
        print("You are allowed to access the system.")
        break
    else:
        print("Your password is incorrect.")
else:
    print("You already got 3 chances. Please try again later.")