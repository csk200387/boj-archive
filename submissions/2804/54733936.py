A, B = input().split()
X, Y = len(A), len(B)
tmp = False
for i in range(X) :
    for l in range(Y) :
        if A[i] == B[l] :
            N,M = i, l
            tmp = True
            break
    if tmp :
        break
for i in range(Y) :
    for l in range(X) :
        if i == M :
            print(A, end="")
            break
        else :
            if l == N :
                print(B[i], end="")
            else :
                print(".", end="")
    print()