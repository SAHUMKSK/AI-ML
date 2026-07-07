# Print only even numbers from a list.

numbers_list = [10, 20, 41, 55, 63, 47, 85, 98, 99, 100]
only_even_number = []
for i in numbers_list:
    if i % 2 == 0:
        print(i)