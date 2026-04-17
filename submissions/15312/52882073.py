ar = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A,B = input(), input()
a,b = [], []
for i in range(3) :
    a.append(ar[ord(A[i])-65])
    a.append(ar[ord(B[i])-65])
while len(a) != 2 :
    for i in range(1, len(a)) :
        b.append((a[i-1] +a[i])%10)
    a = b
    b = []
print(*a, sep="")