a, b, c = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
res = 0
for cnt in range(max(A[1], B[1], C[1])+1):
    tmp = 0
    if A[0] <= cnt < A[1]:
        tmp += 1
    if B[0] <= cnt < B[1]:
        tmp += 1
    if C[0] <= cnt < C[1]:
        tmp += 1
    if tmp == 1:
        res += a
    elif tmp == 2:
        res += b*2
    elif tmp == 3:
        res += c*3
print(res)