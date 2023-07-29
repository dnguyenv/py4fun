import logging
import traceback
def func1():
    try:
        a = [1,2,3]
        val = a[4]

    except IndexError as e:
        logging.error(e,exc_info=True)

def func2():
    try:
        a = [1,2]
        val = a [3]
    except:
        logging.error("The error is: ", traceback.format_exc())

func2()