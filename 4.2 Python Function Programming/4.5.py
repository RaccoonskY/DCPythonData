#Реализуйте два декоратора:
#Декоратор, который записывает в файл log.txt результат декорируемой функции
#Декоратор с параметром, который записывает результат в указанный файл
from functools import  wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open('log.txt','w') as f:
            result = func(*args, **kwargs)
            f.write(str(result))
        return result
    return wrapper

def logger_in(filename):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs): 
            with open(filename, 'w') as f:
                result = func(*args, **kwargs)
                f.write(str(result))
            return result
        return wrapper
    return decorator


@logger_in('logger_in.txt')
@logger
def summator(nums_list):
    return sum(nums_list)

summator([1,2,3,4])