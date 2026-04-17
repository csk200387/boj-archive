import sys
input = lambda:sys.stdin.readline().rstrip()

db = {}
for _ in range(int(input())):
    n, d = input().split("@")
    n = n.replace('.', '').split('+')[0]
    if d in db:
        db[d].append(n)
    else:
        db[d] = [n]

count = 0
for k, v in db.items():
    count += len(set(v))
print(count)