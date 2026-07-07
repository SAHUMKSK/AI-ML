# 6. Print every element using a for loop.

roles = ["AI Engineer", "ML Engineer", "Data Engineer", "Data Analyst", "Data Scientist"]

n = 1
for i in enumerate(roles):
    print(f"Element # {i[0] + 1} is {i[1]}.")