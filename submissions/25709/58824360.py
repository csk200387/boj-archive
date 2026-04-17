def removeone(n) :
    n = str(n)
    if n.count("1") == 0 :
        return int(n)
    n = n[:n.index("1")] + n[n.index("1")+1:]
    return int(n)

n = int(input())
count = 0
while n != 0 :
    if n-1 == 0 :
        count += 1
        break
    n = min(n-1, removeone(n))
    count += 1
print(count)