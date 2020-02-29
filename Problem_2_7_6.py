#Problem 2.7.6

def myMin(L):
    if len(L)==0:
        current=0
    else:
        current = L[0]
        for x in L[1:]:
            if x < current:
                current = x
    return current

myMin([1,2,3,0,-1,0.6])

myMin([])