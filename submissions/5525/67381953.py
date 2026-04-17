import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
size = int(input())
data = input()
comp = 'I' + 'OI' * n
cnt = 0
for i in range(size - len(comp) + 1):
    if data[i:i+len(comp)] == comp:
        cnt += 1
print(cnt)