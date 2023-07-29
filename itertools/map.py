a = [1,2,3,4]

b = map(lambda x: x * 2, a)

print(list(b))

c = [x*2 for x in a]

print(c)

f = filter(lambda x: x%2 == 0,a)
print(list(f))

g = [x for x in a if x%2 == 0]
print(list(g))
from functools import reduce

product_a = reduce(lambda x,y: x*y, a)

print(product_a)

