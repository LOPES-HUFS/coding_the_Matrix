#Problem 2.7.2

def my_list(L): return [list(range(1,i+1)) if i !=0 else [] for i in L] 
my_list([0,1,2,3])