import sys
input = lambda:sys.stdin.readline().rstrip()

arr = []
for i in range(int(input())) :
    a, d, g = map(int, input().split())
    score = a*(d+g)
    if a == d+g :
        arr.append(score*2)
    else :
        arr.append(score)
print(max(arr))