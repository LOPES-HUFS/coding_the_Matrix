#Problem 2.7.5

def myProduct(L):
    current = 1
    for x in L:
        current *= x
    return current

myProduct([2,2,3])