n = int(input())
d=input()
r=0
print(abs(d.count('N')-d.count('S')) + abs(d.count('E')-d.count('W')))