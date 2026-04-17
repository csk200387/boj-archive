l,s = map(int, input().split())
d = input()
a,c,g,t = map(int, input().split())
r = 0
for i in range(s, l+1):
    A,C,G,T = 0,0,0,0
    p = d[i-s:i]
    for j in p:
        if j == 'A':
            A += 1
        elif j == 'C':
            C += 1
        elif j == 'G':
            G += 1
        elif j == 'T':
            T += 1
    if a >= A and c >= C and g >= G and t >= T:
        r += 1
print(r)