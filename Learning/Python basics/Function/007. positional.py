# Positional Arguments: These are the arguments order which you pass them matters strictly.

def studInfo(name, rollno):
    print(f"Roll No # {rollno}")
    print(f"Name : {name}")

studInfo("Mukesh Sahu", 101) # It will pass the values in the same order.
studInfo(101, "Mukesh Sahu") # It will pass the values in the same order.