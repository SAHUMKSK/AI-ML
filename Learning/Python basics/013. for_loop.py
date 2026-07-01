'''
Loop is to used to repeat the block of code for a specific time.
For loop is used to iterate over a sequence(such as list, tuple, or string).

syntax:
for variable in iterable:
    block of code

for variable in range(start, stop, step): except stop rest of the things are optional(default step = 1)
    block of code

'''

for i in range(1, 11, 1): # start = 0, stop = 11, step = 1 
    print(i) # It will print the


print("Print only odd numbers upto 11")
for j in range(1, 11, 2):
    print(j)


for k in enumerate("MUKESH SAHU"):# In k it stores the index and value 
    print(k)