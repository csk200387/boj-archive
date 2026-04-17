import sys
input = lambda:sys.stdin.readline().rstrip()

arr = []
sar = set()
for i in range(int(input())):
    arr.append(input())
    sar.add(arr[i])

s = arr.index("?")
if 0 < s and s < len(arr)-1:
    start = arr[s-1][-1]
    end = arr[s+1][0]
elif s == 0:
    end = arr[s+1][0]
elif s == len(arr)-1:
    start = arr[s-1][-1]


for _ in range(int(input())):
    tmp = input()
    if tmp not in sar:
        if tmp.startswith(start) and tmp.endswith(end):
            print(tmp)
            break