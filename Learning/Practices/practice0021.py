# Search for a number in a list using for...else.

index = int(input("Enter the number of element you want to add in the list: "))

list = []

for i in range(index):
    list.append(int(input(f"Enter the element # {i + 1} : ")))


print(list)



element = int(input("Enter the element you want to check whether it is present or not in that list: "))

list = [10, 20, 30, 40, 50]



for i in list:
    if element == i:
        print("Element found.")
        break


else:
    print("Given number is not present in that list.")

