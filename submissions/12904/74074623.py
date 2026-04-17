d=input()
g=input()
while len(d)<len(g):
 if g[-1]=="A":g=g[:-1]
 else:g=g[:-1][::-1]
print(1 if d==g else 0)