n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = 0
start, end = 0, n - 1
while start < end:
  tmps = arr[start] + arr[end]
  if tmps <= k:
    start += 1
    end -= 1
    s += 1
  else:
    end -= 1
print(s)