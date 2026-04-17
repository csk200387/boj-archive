n = int(input())
for _ in range(n) :
    print("@"*(3*n)+" "*n+"@"*n)
for _ in range(n*3) :
    print("@"*n+" "*n+"@"*n+" "*n+"@"*n)
for _ in range(n) :
    print("@"*n+" "*n+"@"*(3*n))