import sys
input = lambda:sys.stdin.readline().rstrip()

arr = []
sar = set()
for i in range(int(input())):
    arr.append(input())
    sar.add(arr[i])

s = arr.index("?")
start = arr[s-1][-1]
end = arr[s+1][0]

for _ in range(int(input())):
    tmp = input()
    if tmp not in sar:
        if tmp.startswith(start) and tmp.endswith(end):
            print(tmp)
            break