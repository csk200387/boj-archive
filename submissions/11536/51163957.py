import sys
input = lambda:sys.stdin.readline().rstrip()
arr = []
for _ in range(int(input())) :
    arr.append(input())
if sorted(arr) == arr :
    print("INCREASING")
elif sorted(arr, reverse=True) == arr :
    print("DECREASING")
else :
    print("NEITHER")