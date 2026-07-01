# Switch Case or Match Case:

years = int(input("How many years of experiences do you have? "))

match years:
    case 0 | 1 | 2:
        print("You are a fresher.")
    
    case 3 | 4 | 5:
        print("You are an intermediater.")
    
    case 6 | 7 | 8:
        print("You are experienced.")
    
    case 9 | 10 | 11 | 12:
        print("You are pro.")
    case _:
        print("You entered wrong input.")