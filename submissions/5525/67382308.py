import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
size = int(input())
data = input()
comp = 'I' + 'OI' * n
result, cnt, i = 0, 0, 0
while i < size - 1:
    if data[i:i+3] == 'IOI':
        cnt += 1
        i += 2
        if cnt == n:
            cnt -= 1
            result += 1
    else:
        i += 1
        cnt = 0
print(result)