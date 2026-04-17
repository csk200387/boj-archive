input()
A = list(map(int,input().split()))
n = len(A)
lis = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if A[i] > A[j] and lis[i] < lis[j] + 1:
            lis[i] = lis[j] + 1
print(max(lis))