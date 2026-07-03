# Print all Armstrong numbers from 1 to 1000.

list_of_armstrong = []

for i in range(1, 1001):
    total = 0
    string = str(i) # it converted the number to string
    length = len(string) # it stores the length of the number
    
    for j in string: # It will go through all the characters
        total = total + int(j) ** length # 
        
    if i == total:
        list_of_armstrong.append(i)

print(list_of_armstrong)