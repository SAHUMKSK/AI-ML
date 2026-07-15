# 7. Access a list element using an index entered by the user. Handle invalid indices.

list_roles = ["AI Engineer", "ML Engineer", "Data Architect", "Data Analysis", "Data Engineer"]

try:

    index = int(input("Enter the index number you want to see the value: "))
    value = list_roles[index]

except IndexError:
    print("Index is out of range.")

except ValueError:
    print("Only numbers are allowed.")

except:
    print("Something went wrong.")
else:
    print(value)
