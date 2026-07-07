# 1. Append: Adds an element to the end of the list.

roles = ["AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Scientist"]

roles.append("Data Engineer")
print(roles)

# 2. Insert: Adds an element to sapecific position.

roles = ["AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Scientist", "Data Engineer"]

roles.insert(7,"Robotics Engineer")
print(roles)

# 3. Extend: Adds multiple elements.

list1 = [1, 2, 3]
list2 = [6, 7, 8]

print(list1)
print(list2)

list1.extend(list2)

print(list1)
print(list2)


# 4. Remove: It will remove the first matching values form the list. It will throw the error if the value is not exist.

roles = ["AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Scientist", "Data Engineer"]

roles.remove("Data Analyst")
print(roles)


# 5. Pop: It removes the elements using index.

roles = ["AI Engineer", "ML Engineer", "Data Architect", "Data Scientist", "Data Engineer", "Data Analyst"]

removed_balue = roles.pop(5)

print(roles)
print(removed_balue)

# 6. Clear: This method is used to clear the list.

roles = ["AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Scientist", "Data Engineer"]
roles.clear()

print(roles)

# 7. Index: It returns the index value of the given element.

roles = ["AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Scientist", "Data Engineer"]

print(roles.index("Data Architect"))

# 8. Count: It will give the the occurences of the given element.

roles = ["AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Scientist", "Data Engineer"]

print(roles.count("AI Engineer"))

# 9. Sort: It will sort the list in ascending order.

numbers = [10, 50, 30, 40, 60, 90, 100, 80, 70, 20]
numbers.sort()
print(numbers)

# 10. Reverse: It will reverse all the elements.

numbers = [10, 50, 30, 40, 60, 90, 100, 80, 70, 20]
numbers.reverse()
print(numbers)

# 11. List Slicing: To slice the list.

numbers = [10,20,30,40,50]

print(numbers[:3]) # It will print first 3 elements
print(numbers[-2:]) # It will pring last 2 elements
print(numbers[1:4]) # It will pring form 1 to 3 elements
print(numbers[::2]) # It will pring every 2bd elements
print(numbers[::-1]) # It will reverse the list

# 12: Matrix(nested list):

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print()
print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])

print()