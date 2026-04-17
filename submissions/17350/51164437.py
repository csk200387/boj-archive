import sys
input = lambda:sys.stdin.readline().rstrip()
arr = []
for _ in range(int(input())) :
    arr.append(input())
if "anj" in arr :
    print("뭐야;")
else :
    print("뭐야?")