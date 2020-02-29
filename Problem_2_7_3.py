#Problem 2.7.3

def my_function_composition(f,g): return dict(zip(list(f.keys()),list(g.values())))

f = {0:"a",1:'b'}
g = {"a":"apple","b":"banana"}

my_function_composition(f,g)