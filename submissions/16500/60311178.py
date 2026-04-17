S,n,*A = open(0)
S = S.strip()
A = [i.strip() for i in A]
A.sort(key=lambda x: (len(x),x))
for i in A:    
    while i in S :
        S = S.replace(i, '')
if len(S) == 0:
    print(1)
else:
    print(0)