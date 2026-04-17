import sys
input = lambda:sys.stdin.readline().rstrip()

data = set()
for i in range(int(input())) :
    a, b = input().split()
    if b == 'enter' :
        data.add(a)
    else :
        data.remove(a)
print(*sorted(data, reverse=True), sep='\n')