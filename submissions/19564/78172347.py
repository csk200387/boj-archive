st = input()
prev = 0
cnt = 1
for c in st:
    asc = ord(c)
    if prev >= asc:
       cnt += 1
    prev = asc

print(cnt)