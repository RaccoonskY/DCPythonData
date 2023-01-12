#Реализуйте функцию, которая получает в качестве аргумента список чисел
# и преобразует его в список строк.
# Используйте функциональное программирование.

def list_nums_to_char(numlist):
    if numlist is None:
        numlist = list()
    return [str(num) for num in numlist]


print(list_nums_to_char([1,2,3,4,5,6]))