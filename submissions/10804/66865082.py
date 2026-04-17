import sys
input = lambda:sys.stdin.readline().rstrip()
def swap(i, j):
    for k in range((j-i+1)//2):
        arr[i+k], arr[j-k] = arr[j-k], arr[i+k]
arr = list(range(1, 21))
for _ in range(10):
    i, j = map(int, input().split())
    swap(i-1, j-1)
print(*arr)