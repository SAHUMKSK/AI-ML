'''
Loop controls: it is used to conntrol the loops.

1. Break: It will terminates the loop immediately when a specified condition is met.

2. Continue: It stops executing any subsequent code within the current loop block.

'''

print("Break")
for i in range(1, 11):
    
    if i == 6:
        break
    print(i)

print("The loop has been terminated.")

print("Continue")
for i in range(1, 11):
    
    if i == 6:
        continue # Here it will skip this iteration
    
    print(i)


for i in range(1, 6):
    for j in range(1, 6):
        if i == 2 and j == 2:
            print("It terminates the loop.")
            break
        print(i, j)
        print("Inner loop")
    print("Outer loop")