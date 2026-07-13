# 13. Check whether {1,2, 3, 4} is a subset of {1,2}.

setA = {1, 2, 3, 4}
setB = {1, 2}

if setA.issuperset(setB):
    print("Set A is the superset of Set B.")
else:
    print("Set A is not the superset of Set B.")