*a,_=map(float,open(0))
print(*[f"{a[i]-a[i-1]:.2f}"for i in range(1,len(a))],sep="\n")