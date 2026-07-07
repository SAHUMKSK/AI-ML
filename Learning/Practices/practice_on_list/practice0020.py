# 20. Create a list containing multiples of 5 from 5 to 100.

multiply_of_5 = []

for i in range(1, 101):
    if i % 5 == 0:
        multiply_of_5.append(i)

print(multiply_of_5)