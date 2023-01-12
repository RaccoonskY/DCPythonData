# написать функцию, превращающую список чисел в список строк
import random


int_list  = [ random.randint(0,10) for num in range(0,random.randint(1,11))]
print(int_list)
char_list = list(map(lambda x: str(x),int_list))
print((char_list))
