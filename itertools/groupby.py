from itertools import groupby

a = [1,2,3,4]

persons = [{'name': 'Tim', 'age': 25},{'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27}, {'name': 'Clair', 'age': 28}]

def smaller_than_3(x):
    if x< 3:
        return 'Duy'
    else:
        return 'Hoa'
group_obj = groupby(a,key=smaller_than_3)
group_obj1 = groupby(a,key=lambda x: x < 2)

for key,value in group_obj:
    print(key,list(value))

for key, value in group_obj1:
    print(key,list(value))

group_person = groupby(persons, key=lambda x: x['age'])

for key, value in group_person:
    print(key, list(value))