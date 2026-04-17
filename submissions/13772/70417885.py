s = {'A', 'D', 'O', 'P', 'Q', 'R'}
n = int(input())
for _ in range(n):
    cnt = 0
    data = input()
    for i in data:
        if i in s:
            cnt += 1
        elif i == 'B':
            cnt += 2
    print(cnt)