#Problem 2.7.1

def my_filter(L,num): return [i for i in L if i/num != int(i/num)]

my_filter([1,2,4,5,7],2)