import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for i in range(n):
    data = input()
    isp = True
    cnt = 1
    for j in range(len(data)//2):
        if data[j] != data[-1-j]:
            isp = False
            break
        cnt += 1
    print(int(isp), cnt)