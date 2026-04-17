n,*arr=map(int,open(0))
t=sum(arr)-n*(arr[-1]*2-n+1)//2
print(0 if t else t)