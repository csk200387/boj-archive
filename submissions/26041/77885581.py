arr = input().split()
s = input()
cnt = 0
for i in arr:
  if i.startswith(s) and len(i) > len(s):
    cnt += 1
print(cnt)