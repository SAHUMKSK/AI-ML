'''

Arbitrary positional arguments: It allows n numbers of possitional arguments. This is useful when you do no know beforehand how many values a user will pass into the function.


'''

def userInput(*Input):
    print(type(Input))
    print(Input)

userInput(10, 20, 30, 40)