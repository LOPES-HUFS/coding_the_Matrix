#Problem 2.7.8

def myUnion(L):
    current = []
    for i in L:
        current += list(i)
    current = set(current)
    return current

t=[{1,2,3,0},{4,5,2,3}]

myUnion(t)

myUnion([])