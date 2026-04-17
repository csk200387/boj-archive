a, b = map(int,input().split())
ar = []
for i in range(a) :
    ar.append(input())
print(sorted(ar)[b-1])