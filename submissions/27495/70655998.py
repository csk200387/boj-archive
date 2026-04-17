import sys
input = lambda:sys.stdin.readline().rstrip()

arr = [input().split() for _ in range(9)]

d = {}
for i in range(3):
    for l in range(3):
        if i == 1 and l == 1:
            continue
        val = []
        for x in range(3*i, 3*i+3):
            for y in range(3*l, 3*l+3):
                if x == (3*i+1) and y == (3*l+1):
                    key = arr[x][y]
                else:
                    val.append(arr[x][y])
        d[key] = sorted(val)

for idx, key in enumerate(sorted(d)):
    print(f"#{idx+1}. {key}")
    for i, v in enumerate(d[key]):
        print(f"#{idx+1}-{i+1}. {v}")