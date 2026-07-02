'''
Loop else: Loop else will execute when the entire loop executed.
NOTE: If the loop breaks in between else block will not execute.


'''

for i in range(11):
    print(i)
else:
    print("Loop executed successfully.")

for j in range(11):
    if j == 6:
        print("Loop has been stopped")
        break
    print(j)
else:
    print("Loop executed successfully.")


for k in range(11):
    if k == 6:
        print("Skipped")
        continue
    print(k)
else:
    print("Loop executed successfully.")


l = 1
while(l <=10):
    print(l)
    l += 1
else:
    print("Loop executed successfully.")

m = 1
while(m <=10):
    if m == 6:
        print("Loop has been stopped.")
        break
    print(m)
    m += 1
else:
    print("Loop executed successfully.")