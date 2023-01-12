sum = 0

f = open('numbers.txt', 'r')
my_gen_nums = (int(i) for i in f.read().split(' '))

for i in my_gen_nums:
    sum+= i

print(sum)