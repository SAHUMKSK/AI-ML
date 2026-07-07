# 9. Find the largest number without using min().

numbers_list = [100, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -10000, 1000]
small = numbers_list[0]
for i in numbers_list:
    if i < small:
        small = i
    
print(f"Smallest number is {small}.")
