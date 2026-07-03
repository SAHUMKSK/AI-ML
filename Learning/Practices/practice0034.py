# Check whether a number is a strong number.

number = int(input("Enter the number to check whether the number is strong number or not: "))

if number < 0:

    print("You entered the negative number.")

else:
    
    factorial = []
    
    for i in str(number):
        
        total = 1

        if 0 == int(i):

            factorial.append(1)

        else:

            for j in range(int(i), 0, -1):
                
                total *= j

            factorial.append(total)

    if number == sum(factorial):

        print("Entered number is a strong number.")

    else:

        print("Entered number is not a strong number.")
    