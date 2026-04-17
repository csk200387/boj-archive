N, A, B = map(int, input().split())
if A < B+N :
    print("Bus")
elif A == B == N:
    print("Anything")
else:
    print("Subway")