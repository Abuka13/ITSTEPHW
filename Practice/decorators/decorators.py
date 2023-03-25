import time
import datetime
def decorator_rounding(func):
    def wrapper(*args, **kwargs): #args - Позиционные , key-word args - именные
        # print(args)
        # print(kwargs)
        # print(func)
        result = func(*args,**kwargs)

        result = round(result, 2)
        return result


    return wrapper
@decorator_rounding
def summing(value1, value2, value3):
    print("summing")
    res = value1 + value2 + value3
    return res
@decorator_rounding
def divider(value1, value2):
    res = value1 / value2
    return res

print(summing(-12, 17.0006, 1))
print(divider(-12, -17)) #todo ПОЗИЦИОННЫЕ не работает без args
print(divider(value1 = -12, value2 = -17)) #TODO Именные -- не работает без kwargs
