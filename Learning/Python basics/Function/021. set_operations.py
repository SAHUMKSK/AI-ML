# Set operations:

# 1. Unions: It combine all the unique values.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
unionSet = a | b
print(unionSet)

# 2. Intersections: It returns only the elemnets that are common to all sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
intersectionSet = a & b
print(intersectionSet)

# 3. Difference: It returns a new set containing elements that exist in first set and bot in the 2nd set. 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

differenceSet = a - b
print(differenceSet)

# 4. Symmetric Difference: It returns a new set containing elements that are in either of sets, but NOT in both.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

simmetricDifference = a ^ b
print(simmetricDifference)