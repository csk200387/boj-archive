N, A, B = map(int, input().split())
if B == N:
    if B == A:
        print("Anything")
    else:
        print("Subway")
elif A < B+N:
    print("Bus")
else :
    print("Subway")