from functools import cmp_to_key
def comp(x, y):
    if int(x+y) > int(y+x):
        return -1
    if int(x+y) < int(y+x):
        return 1
    return 0
input()
arr = input().split()
arr.sort(key=cmp_to_key(comp))
print(int("".join(arr)))