# Print all numbers between 1 and 100 that are divisible  by both 3 and 5.

divisible  = []
for i in  range(1, 101):
    if (i % 3 == 0 ) and ( i % 5 == 0 ):
        divisible .append(i)
print("All the numbers are divisible  by 3 and 5.")
print(divisible)
