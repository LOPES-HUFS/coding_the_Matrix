#Problem 2.7.4

def mySum(L):
    current = 0
    for x in L:
        current += x
    return current

mySum([0,1,2,3])