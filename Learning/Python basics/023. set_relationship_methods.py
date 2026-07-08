# 1. issubset: It returns True if all the elements of given set are present in another super set.

a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(a.issubset(b))

# 2. issuperset: It returns True if a set contains all the elements of another specified collection. returns True if all the elements of given set are present in another super set.

a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(b.issuperset(b))

# 3. isdisjoint: It returns True if both sets have no common elements.

a = {1, 2, 3}
b = {4, 5, 6}

print(a.isdisjoint(b))

# Frozenset: A set can not be modified after creation.

set_a = frozenset({1, 2, 3})

print(set_a)