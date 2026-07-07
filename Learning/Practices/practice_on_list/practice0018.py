# 18. Count how many times a number appears.
number_list = [4, 1, 2, 1, 4, 4, 1, 2, 8, 1]
counts = {}

for i in number_list:
    
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

for i in counts:
    if counts[i] == 1:
        print(f"{i} comes {counts[i]} time.")
    else:
        print(f"{i} comes {counts[i]} times.")