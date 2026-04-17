N, A, B = map(int, input().split())
if A == B == N:
    print("Anything")
elif A < B+N:
    print("Bus")
else :
    print("Subway")