try:
    a = 5/1
    b = a + '10'
except Exception as e:
    print(e)
except TypeError as te:
    print(te)
else:
    print('Everything is fine')
finally:
    print('Cleaning up')