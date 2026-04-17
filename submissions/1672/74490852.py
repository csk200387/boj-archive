arr =  [['A', 'C', 'A', 'G'],
        ['C', 'G', 'T', 'A'],
        ['A', 'T', 'C', 'G'],
        ['G', 'A', 'G', 'T']]
t = 'AGCT'
input()
d = list(input())

while len(d) > 1:
    a = d.pop()
    b = d.pop()
    d.append(arr[t.index(b)][t.index(a)])
print(*d)