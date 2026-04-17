n = int(input())
count = 0
while n != 0 :
    if n-1 == 0 :
        count += 1
        break
    n = min(n-1, int(str(n).replace("1","")))
    count += 1
print(count)