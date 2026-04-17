num = int(input())
ar = []
for i in range(num) :
    ar.append(list(map(int,input().split())))

ar.sort(key=lambda x:(x[0], x[1]))
for i in ar :
    print(" ".join(map(str,i)))