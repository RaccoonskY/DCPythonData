import random
import string

n = 10

char_list_first = []
char_list_second = []

dict_first = {}
dict_second = {}

char_list_first.append(random.choice(string.ascii_lowercase))
char_list_second.append(random.choice(string.ascii_lowercase))

for i in range(n):
    char_list_first.append(random.choice(string.ascii_lowercase))
    dict_first[i] = char_list_first[i]

    char_list_second.append(random.choice(string.ascii_lowercase))
    dict_second[i] = char_list_second[i]

print(f'LIST:{char_list_first}\nDICT:{dict_first}\n\nLIST:{char_list_second}\nDICT:{dict_second}')

dict_first = dict(zip())