'''
List is built in collection data type used to store an ordered, mutable sequence of items.

syntax : variable_name = [value_1, value_2, value_3, ..., value_n]

example 1:
    fruits = ["Apple", "Banana", "Cherry", "Date"]

example 2:
    list = ["Mukesh Sahu", "AI/ML Engineer", 30, True]

'''
fruits = ["Apple", "Banana", "Cherry", "Date"]

print(fruits)

print(fruits[0]) # Access using index

fruits.append("Elderberry") # Add items using append method

print(fruits)

fruits.remove("Cherry") # Remove items using remove method

print(fruits)

fruits[2] = "Orange" # Replace the item by passing the index number

print(fruits)

print("Apple" in fruits) # It will check whether the given value is exist or not in that list.