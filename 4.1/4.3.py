import os.path


def get_sum_file(infile,outfile):
    inputfile = open(infile,'r')
    numbers = inputfile.readlines()
    sum = 0
    for i in numbers:
        sum += int(i)
    print(sum)
    outfile = open(outfile, 'a').writelines('\n'+str(sum))


get_sum_file('numbers.txt','answers.txt')
print(os.path.abspath('numbers.txt'))
print(os.path.relpath('numbers.txt'))
