'''
Dictionary is build in data structure used to store the values in key : valye pairs.

syntax : variable_name = [key_1 : value_1, key_1 : value_2, key_3 : value_3, ..., key_n : value_n]

example 1:
    cgpa_of_students = ["Stephen Carter" : 7.7,  "Johny Carter": 8.8, "Steve Carter" : 9.9, "Jessica Carter" : 9.0 ]

example 2:
    list = ["Mukesh Sahu", "AI/ML Engineer", 30, True]

'''

cgpa_of_students = {"Stephen Carter" : 7.7,  "Johny Carter": 8.8, "Steve Carter" : 9.9, "Jessica Carter" : 9.0 }

print(cgpa_of_students)

print(cgpa_of_students["Jessica Carter"]) # By passing the key

print(len(cgpa_of_students)) # Number of key value pairs

print(type(cgpa_of_students))

cgpa_of_students["John Carter"] = 6.6 # Inster a new value by passing the new key if the key is already exist it will update the value for given key.

print(cgpa_of_students)

cgpa_of_students.pop("Johny Carter") # Delete the key and value using pop method

print(cgpa_of_students)




for i in cgpa_of_students: # Printing the values using loop
    print(i, ":" ,cgpa_of_students[i])