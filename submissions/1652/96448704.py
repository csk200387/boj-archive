import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
arr = []
w, l = 0, 0
for i in range(n):
    arr.append(input())

for x in range(n):
    t_arr = []
    for y in range(n):
        if arr[x][y] == ".":
            t_arr.append(0)
        if arr[x][y] == "X" or y == n-1:
            if len(t_arr) >= 2:
                w += 1
            t_arr = []

for y in range(n):
    t_arr = []
    for x in range(n):
        if arr[x][y] == ".":
            t_arr.append(0)
        if arr[x][y] == "X" or x == n-1:
            if len(t_arr) >= 2:
                l += 1
            t_arr = []
print(w, l)