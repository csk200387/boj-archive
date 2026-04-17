import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
arr = [int(input()) for _ in range(n)]
diffs_a = [arr[i] - arr[i-1] for i in range(1, n)]
diffs_g = [arr[i] // arr[i-1] for i in range(1, n)]

if diffs_a.count(diffs_a[0]) == len(diffs_a):
    print(arr[-1] + diffs_a[-1])
else:
    print(arr[-1] * diffs_g[-1])