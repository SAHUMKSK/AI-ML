# 4. Print all multiples of 7 between 1 and 100.


for i in range(0, 101, 7):
    print(i)


print("All the numbers are multiples by 7")
for j in range(101):
    if j % 7 == 0:
        print(j)
