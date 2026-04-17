import sys
input = lambda:sys.stdin.readline().rstrip()

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

min_time = 1e9
max_height = 0
for i in range(n):
    for j in range(m):
        max_height = max(max_height, land[i][j])

for height in range(max_height+1):

    block = b
    time = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] > height:
                block += land[i][j] - height
                time += (land[i][j] - height) * 2
            elif land[i][j] < height:
                block -= height - land[i][j]
                time += height - land[i][j]

    if block >= 0:
        if time <= min_time:
            min_time = time
            result_height = height

print(min_time, result_height)