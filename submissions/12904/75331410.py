d,g=input(),input()
while len(d)<len(g):
 if g[-1]=="A":g=g[:-1]
 else:g=g[:-1][::-1]
print(int(d==g))