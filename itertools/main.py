from itertools import product

a = [1,2]
b = [3,4]

prod = product(a,b)

print(list(prod))

prod1 = product(a,b, repeat = 2)

print(list(prod1))