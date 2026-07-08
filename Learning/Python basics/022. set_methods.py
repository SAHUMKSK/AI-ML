# Set Methods:

# 1. Update: Add multiple elements to the set from another iterable(list, set, tuple, string etc.)

techRoles = {"AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Engineer"}

techRoles.update(("AI Researcher", "NLP Engineer", "Robotics Engineer", "Computer Vision Engineer"))

print(techRoles)

# 2. Remove: It removes the specific element.

techRoles = {"AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Engineer"}

techRoles.remove("Data Engineer")
# techRoles.remove("Data Scientist") # It will throw an error like KeyError if the value doesn't exist.

print(techRoles)

# 3. Discard: It also removes the specific element but it will not throw any error if the value doesn't exist.

techRoles = {"AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Engineer"}

techRoles.discard("Data Analyst")
techRoles.discard("Dummy Roles")
print(techRoles)

# 4. Pop: It will remove a random element from that set.

techRoles = {"AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Engineer"}

techRoles.pop()

print(techRoles)

# 5. Clear: It removes all the elements form the given set.

techRoles = {"AI Engineer", "ML Engineer", "Data Architect", "Data Analyst", "Data Engineer"}

techRoles.clear()

print(techRoles)