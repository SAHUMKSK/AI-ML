''' 16. Print the union, intersection, difference of (A - B) and (B - A), symmetric difference.
Given:
A = {1,2,3,4,5}
B = {4,5,6,7,8}
'''

A = {1,2,3,4,5}
B = {4,5,6,7,8}

print(f"Union of A and B: {A | B}")
print(f"Intersection of A and B: {A & B}")
print(f"Difference of A and B: {A - B}")
print(f"Difference of B and A: {B - A}")
print(f"Symmetic difference of A and B: {A ^ B}")