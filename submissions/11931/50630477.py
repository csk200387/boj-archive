num = int(input())
r = []
for i in range(num) :
    a = int(input())
    r.append(a)
r.sort(reverse=True)
for i in r :
    print(i) 