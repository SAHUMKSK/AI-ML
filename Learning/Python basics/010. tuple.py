'''
List: List is built in collection data type used to store an ordered, immutable sequence of items.

syntax : variable_name = (value_1, value_2, value_3, ..., value_n)

example 1:
    subjects = ("Maths", "Psysics", "Chemistry", "English")


example 2:
    tuple = ("Mukesh Sahu", "AI/ML Engineer", 30, True)

'''
empID = (101, 102, 103, 104, 105, 106, 107, 108, 109, 110)

subjects = ("Maths", "Psysics", "Chemistry", "English")

print(subjects)

print(subjects[0]) # Access using index

print(type(subjects))

for i in subjects: # Print all the subjects using loop
    print(i)


# Tuple packing: To pack in single element.

empInfo = 101, "Mukesh Sahu", "AI Engineer", "Surat"

print(empInfo)

# Tuple unpacking: To unpack into multiple elements.

empID, empName, empRole, empCity = empInfo

print(empID)
print(empName)
print(empRole)
print(empCity)

shape = (1000, 20)

