import sys
input = lambda:sys.stdin.readline().rstrip()

arr = [0.0, 0.7, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 4.3]

def closet(G):
    tmp = [round(abs(float(G) - val), 3) for val in arr]
    mint = min(tmp)
    indx = tmp.index(mint)
    return arr[indx]

for _ in range(int(input())) :
    C, G = 0, 0
    n = int(input())
    for i in range(n) :
        A, B = map(float, input().split())
        C += A
        G += A*B
    print(int(C), closet(G/C))