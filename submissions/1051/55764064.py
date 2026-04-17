import sys
input = lambda:sys.stdin.readline().rstrip()

n,t = map(int, input().split())
arr = []

for _ in range(n) :
    arr.append(input())

default = 1
result = []
for default in range(max(len(arr), len(arr[0]))) :
    for i in range(len(arr)) : # 세로
        for l in range(len(arr[0])) : # 가로
            try :
                if arr[i][l] == arr[i][l+default] == arr[i+default][l] == arr[i+default][l+default] :
                    result.append(default)
            except IndexError :
                pass
print((max(result)+1)**2)