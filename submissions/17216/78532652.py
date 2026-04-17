n = int(input())
A = list(map(int,input().split()))
lis = [1] * n
lis[0] = A[0]
for i in range(1, n):
    for j in range(i):
        if A[i] < A[j]:
            lis[i] = max(lis[i], lis[j] + A[i])
        else:
            lis[i] = max(lis[i], A[i])
print(max(lis))