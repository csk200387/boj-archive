import sys
input = sys.stdin.readline

n = int(input().rstrip())
for i in range(n) :
    yon, kor = 0, 0
    for l in range(9) :
        a, b = map(int, input().rstrip().split())
        yon += a
        kor += b
    if yon > kor :
        print("Yonsei")
    elif yon < kor :
        print("Korea")
    else :
        print("Draw")