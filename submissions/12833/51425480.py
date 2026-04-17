A, B, C = map(int, input().split())
A, B = bin(A), bin(B)
for _ in range(C) :
    A = bin(int(A, 2) ^ int(B, 2))
print(int(A,2))