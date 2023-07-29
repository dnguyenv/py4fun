from collections import Counter

test_string = 'aaabbbbcccddddd'

test_counter = Counter(test_string)

print(test_counter) # Counter({'d': 5, 'b': 4, 'a': 3, 'c': 3})
print(test_counter.most_common()) # [('d', 5), ('b', 4), ('a', 3), ('c', 3)]
print(test_counter.most_common(1)) # [('d',5)]

test_list = list(test_counter)

print(test_list) # ['a', 'b', 'c', 'd']

test_list_elements = list(test_counter.elements())

print(test_list_elements) # ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']