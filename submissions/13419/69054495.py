import sys
input = lambda:sys.stdin.readline().rstrip()
for i in range(int(input())):
    data = input()
    length = len(data)
    if length % 2 == 0:
        print(data[::2])
        print(data[1::2])
    else:
        print((data*2)[::2])
        print((data*2)[1::2])