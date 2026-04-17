import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
size = int(input())
data = input()
comp = 'I' + 'OI' * n

cnt = 0
i = 0
while i < size - len(comp) + 1:
    if data[i:i+len(comp)] == comp:
        cnt += 1
        i += 2
    else:
        i += 1
print(cnt)