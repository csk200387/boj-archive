import sys
num = int(input(""))
for i in range(0,num):
    data = list(map(int,sys.stdin.readline().rstrip("\n").split()))
    print(data[0]+data[1])