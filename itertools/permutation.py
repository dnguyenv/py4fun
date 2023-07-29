from itertools import permutations

a = [1,2,3]
permutation_test = permutations(a)
permutation_test1 = permutations(a, 2)
print(list(permutation_test))
print(list(permutation_test1))