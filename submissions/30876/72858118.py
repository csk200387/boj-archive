a,*arr=open(0)
print(min(arr,key=lambda x:int(x.split()[1])),end="")