# 9. Find the largest number without using max().

numbers_list = [100, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -10000, 1000]
max = numbers_list[0]
for i in numbers_list:
    if i > max:
        max = i
    
print(f"Largest number is {max}.")
