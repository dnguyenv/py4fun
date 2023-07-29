from itertools import accumulate

import operator

a = [1,2,5,3,4]

acc = accumulate(a)

acc1 = accumulate(a, func=max)

print(a)
print(list(acc))

print(list(acc1))
