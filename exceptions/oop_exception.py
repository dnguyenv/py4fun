class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def exception_test(value):
    if value < 5:
        raise ValueTooSmallError('Value is too small ', value)

try:
    exception_test(2)
except ValueTooSmallError as e:
    print(f'{e.message}: {e.value} ')
finally:
    print('Xong roi may a')