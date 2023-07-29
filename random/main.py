import random
import secrets

def random_test():
    a = random.random()
    return a
def random_uniform():
    b = random.uniform(1,10)
    return b

def random_randint():
    return random.randint(1,10)

def random_randrange():
    r = random.randrange(1 , 10)
    return r
def random_normalvariate():
    return random.normalvariate(0,1)

def random_sample():
    mylist = list('ABCDEFGH')
    a = random.sample(mylist, 3)
    return a
def random_choices():
    mylist = list('ABCDEFGH')
    a = random.choices(mylist, k=3)
    return a

def random_shuffle():
    mylist = list('ABCDEFGH')
    return random.shuffle(mylist)
def random_seed():
    random.seed(1)
    print(random.random())
    print(random.randint(1,10))
    random.seed(2)
    print(random.random())
    print(random.randint(1,10))
    random.seed(1)
    print(random.random())
    print(random.randint(1,10))
    random.seed(2)
    print(random.random())
    print(random.randint(1,10))

def secrets_gen():
    a = secrets.randbits(4)
    print(a)

    mylist = list('ABCDEFG')
    b = secrets.choice(mylist)

    print(b)


import numpy as np

def numpy_func():
    a = np.random.randint(0,10,(2,3))
    b = np.array([[1,2,3],[4,5,6],[7,8,9]])

    print(a)
    print(b)
    np.random.shuffle(b)
    print(b)



numpy_func()





secrets_gen()
#random_seed()

# print(f'Random shuffle: {random_shuffle()}')
#
# print (f'Random choices: {random_choices()}')
#
# print(random_test())
# print(random_uniform())
#
# print(random_randint())
# try:
#     print(random_randrange())
# except Exception as e:
#     print(e)

# print(f'Random normalvariate: {random_normalvariate()}')
#
# print (f'Random example: {random_sample()}')