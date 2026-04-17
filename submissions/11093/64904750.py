import math
n = int(input())
for i in range(n):
    arr = []
    data = input()
    size = math.ceil(len(data) ** 0.5)
    data = data.ljust(size**2, "*")
    arr = [data[j*size:j*size+size] for j in range(size)]
    for j in range(size):
        for k in range(1, size+1):
            if arr[-k][j] != "*":
                print(arr[-k][j], end="")
    print()