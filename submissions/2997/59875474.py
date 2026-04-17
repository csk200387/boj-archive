a,b,c=sorted(map(int,input().split()))
print(c-a+b if b-a>=c-b else c-b+a)