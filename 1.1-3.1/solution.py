import sys

countRows = int(sys.argv[1])
symbol = '#'

n = 1
while n <= countRows:
    print((countRows-n)*' '+n*symbol)
    n += 1

