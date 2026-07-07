# 17. Print the list in reverse using indexing.

roles = ["AI Engineer", "ML Engineer", "Data Engineer", "Data Analyst", "Data Scientist"]

for i in range(len(roles) - 1, -1, -1):
    print(roles[i])