import sys
input = lambda:sys.stdin.readline().rstrip()

size = int(input())
arr = list(map(float, input().split()))
arr.sort(reverse=1)
while len(arr) > 1:
    arr[0] += arr.pop()/2

print(arr[0])