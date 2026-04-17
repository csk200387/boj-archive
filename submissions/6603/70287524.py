from itertools import *
while True:
    a = input()
    if a == "0":break
    arr = list(map(int, a.split()))[1:]
    for i in combinations(arr, 6):
        print(*i)
    print()