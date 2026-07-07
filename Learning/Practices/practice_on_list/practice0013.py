# 13. Count how many even numbers are in a list.

count = 0
numbers_list = [1, 4, 8, 11, 17, 22, 26, 28, 33, 38, 41, 49, 50]
for i in numbers_list:
    if i % 2 == 0:
        count += 1
    
print(f"Total even numbers {count}")
