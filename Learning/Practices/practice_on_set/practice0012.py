# 12. Check whether {1,2} is a subset of {1,2,3,4}.

setA = {1, 2}
setB = {1, 2, 3, 4}

if setA.issubset(setB):
    print("Set A is the subset of Set B.")
else:
    print("Set A is not the subset of Set B.")