input()
t=sum(map(int,input().split()))
print(['Stay','Right','Left'][(t>0)-(t<0)])