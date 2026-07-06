# Arbitrary Keyword Arguments: It allows to accept any number of nam,ed arguments(keyword = value).

def empInfo(fname, lname, **empInfoOptional):
    print(fname)
    print(lname)
    print(empInfoOptional)
    print(type(fname))
    print(type(lname))
    print(type(empInfoOptional))


empInfo(fname = "Mukesh", lname = "Sahu", role = "AI/ML Engineer", salary = 100000)