import functools

def my_decorator(func):

    @functools.wraps(func)
    def my_wrapper(*args, **kwargs):
        print('Before')
        result = func(*args, **kwargs)
        print('After')
        return result
    return my_wrapper

@my_decorator
def print_name(name):
    print(f'Hello {name}')

print_name('Duyhard')
