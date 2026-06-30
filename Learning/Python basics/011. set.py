'''
Set is build in data type used to store unordered collection of unique items.

syntax:
variable_name = {value_1, value_2, value_3, ..., value_n}

i.e.:
set = {07, "Mukesh Sahu", 100000, "AI/ML Engineer"}
'''

set = {7, "Mukesh Sahu", 100000, "AI/ML Engineer"}

print(set)

print(type(set))

set.add("Banglore") # Using add method we can insert the values into a set

print(set)

set.remove("Banglore") # Using remove method we can delete the values from a set. Buit it will give you the error if the value doesn't exists.

print(set)

set.discard(100000) # Using discard method also we can delete the values from a set it will not throw any kind of error if the same value doesn't exists.

print(set)

removed_element = set.pop() # It will removes and returns the random element. 

print(removed_element)
print(set)

set.clear() # It will clear the entire set.

print(set)