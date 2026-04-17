A, B, C = map(int, input().split())
A, B = bin(A), bin(B)
if C%2 == 1 :
    print(int(bin(int(A, 2) ^ int(B, 2)),2))
else :
    print(int(A,2))