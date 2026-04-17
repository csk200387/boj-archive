r,l=[],[]
for i in range(int(input())) :
 x,y=map(int,input().split(","))
 r+=[x]
 l+=[y]
print(f"{min(r)-1},{min(l)-1}")
print(f"{max(r)+1},{max(l)+1}")