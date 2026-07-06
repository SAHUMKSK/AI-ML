# Write a function square(num) that returns the square of a number.

def square(number):
    return number * number

result = square(10)
print(f"Square of the given number is {result}.")

# 2. Write a function that takes a string and returns the count of vowels and consonants separately.

def count_vowels_and_constants(string: str):

    countVowels = 0
    countConsonants = 0

    for eachChar in string:
        if eachChar.isalpha():

            if eachChar in "aeiouAEIOU":
                countVowels += 1
            else:
                countConsonants += 1
    return countVowels, countConsonants

vowels, consonants = count_vowels_and_constants(input("Enter the string to count the vowels and constants: "))

print(f"Total vowels characters are {vowels}.")
print(f"Total vowels characters are {consonants}.")

# 3. Define a function convert_to_upper(word) that returns the uppercase version of the string.

def convert_to_upper(word: str):
    return word.upper()

upper_text = convert_to_upper(input("Enter the string to convert into the upper case: "))
print(upper_text)

# 4. Create a function full_name(fname, lname) that returns the full name joined with a space.

def full_name(fname: str, lname: str):
    return f"{fname} {lname}"

fullname = full_name("Mukesh", "Sahu")
print(fullname)