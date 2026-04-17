l,s = map(int, input().split())
d = input()
a,c,g,t = map(int, input().split())
r = 0
D={'A':0,'C':0,'G':0,'T':0}
for i in range(s):
    if d[i] == 'A':
        D['A'] += 1
    elif d[i] == 'C':
        D['C'] += 1
    elif d[i] == 'G':
        D['G'] += 1
    elif d[i] == 'T':
        D['T'] += 1

if D['A'] >= a and D['C'] >= c and D['G'] >= g and D['T'] >= t:
    r += 1

for i in range(s,l):
    if d[i] == 'A':
        D['A'] += 1
    elif d[i] == 'C':
        D['C'] += 1
    elif d[i] == 'G':
        D['G'] += 1
    elif d[i] == 'T':
        D['T'] += 1
    
    if d[i-s] == 'A':
        D['A'] -= 1
    elif d[i-s] == 'C':
        D['C'] -= 1
    elif d[i-s] == 'G':
        D['G'] -= 1
    elif d[i-s] == 'T':
        D['T'] -= 1
    if D['A'] >= a and D['C'] >= c and D['G'] >= g and D['T'] >= t:
        r += 1

print(r)