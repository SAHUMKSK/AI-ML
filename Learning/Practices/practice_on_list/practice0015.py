# 15. Calculate the sum of all elements without using sum().

total = 0
numbers_list = [1, 4, 8, 11, 17, 22, 26, 28, 33, 38, 41, 49, 50]
for i in numbers_list:
    total += i
    
print(f"Sum of all the elements is {total}.")