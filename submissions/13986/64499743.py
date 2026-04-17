import sys
input = lambda:sys.stdin.readline().rstrip()
h,s = map(int, input().split())
arr = [list(input()) for _ in range(h)]
for i in range(h-2, -1, -1):
    for j in range(s):
        if arr[i][j] == 'o':
            for k in range(i+1, h):
                if arr[k][j] == '.':
                    arr[k-1][j] = '.'
                    arr[k][j] = 'o'
                else:
                    break
print('\n'.join([''.join(i) for i in arr]))