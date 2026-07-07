'''
List is built in collection data type used to store an ordered, mutable sequence of items.

syntax : variable_name = [value_1, value_2, value_3, ..., value_n]

example 1:
    fruits = ["Apple", "Banana", "Cherry", "Date"]

example 2:
    list = ["Mukesh Sahu", "AI/ML Engineer", 30, True]

'''
fruits = ["Apple", "Banana", "Cherry", "Date"]
roles = list(["AI/ML Engineer", "ML Engineer", "AI ENgineer", "Data Analyst", "Data Engener"])

print(fruits)
print(roles)

# Create empty list

emptyList1 = []
emptyList2 = list()

# Access using index

print(fruits[0]) # Access using index
print(fruits[-1]) # Using negative indexing

# Length of the list
print(len(fruits))
print(len(roles))

# Add values
fruits.append("Grapes")
print(fruits)

# Update the values using index
fruits[3] = "Mango"
print(fruits)

# Delete the values using index
print(fruits.pop(3))
print(fruits)

# Delete using value
fruits.remove("Cherry")
print(fruits)

# Concatenate two lists.
new_list = fruits + roles
print(new_list)