def func1():
    x = 5
    if x > 0:
        raise Exception('x should be negative')

def func2():
    x = 5
    assert(x < 0), 'x is not negative'

def func3():
    my_dict = {'name': 'Max'}
    print(my_dict['age'])

def func4():
    try:
        a = 5/0
#    except:
#        print("don't divide by zero")
    except Exception as e:
        print(e)

func4()