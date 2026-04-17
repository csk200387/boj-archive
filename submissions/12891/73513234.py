l,s = map(int, input().split())
d = input()
a,c,g,t = map(int, input().split())
r = 0
for i in range(s, l+1):
    p = d[i-s:i]
    if p.count('A') >= a and p.count('C') >= c and p.count('G') >= g and p.count('T') >= t:
        r += 1
print(r)