A, B = map(int, input().split())
C = B - 45
if(C < 0):
    A -= 1
    if(A < 0): A = 23
    C += 60
print(A,C)