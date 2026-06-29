# It evalute expressions in a boolean context and return eiother true, false or evaluted values.

age = 30
has_license = True

if age >= 18 and has_license == True:

    print('You are allowed to drive.')
    print()


day = "Sunday"


if day == "Sunday" or day == "sunday" or day == "Saturday" or day == "saturday":
    print('It is weekend.')
    print()


is_logged_out = False

if not is_logged_out:
    print("You are currently logged in.")
    print()



