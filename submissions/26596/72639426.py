import sys
input = lambda:sys.stdin.readline().rstrip()
d = {}
for i in range(int(input())):
    k,v = input().split()
    if k in d:d[k] += int(v)
    else:d[k] = int(v)
for k,v in sorted(d.items(), key=lambda x:x[1]):
    if int(v*1.618) in d.values():
        print("Delicious!")
        exit()
print("Not Delicious...")