# 8. Access a dictionary value using a key entered by the user. Handle missing keys.

country_capitals = {
    "India" : "Delhi", 
    "England": "London", 
    "U.S.A.": "Washington", 
    "Australia": "Canberra", 
    "New Zealand": "Wellington"
    }


try:
    key = input("Enter the key to know the value: ")

    value = country_capitals[key]

except KeyError:
    print("Your entered key is not exist.")
except:
    print("Something went wrong.")
else:
    print(value)