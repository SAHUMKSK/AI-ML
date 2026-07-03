# Count vowels and consonants in a string.

string = input("Enter your string to count vowels and constants: ")
vowels = 0
constants = 0
for i in string:
    if i.isalpha():
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            vowels = vowels + 1
        else:
            constants = constants + 1

print("Total number of vowels:", vowels)
print("Total number of constants:", constants)
