n = int(input())
f = 0
while 1:
 f+=1
 s=int(f*(f+1)/2)
 if s>=n:break
arr = [f"{i+1}/{f-i}" for i in range(f)]
if n==1:print("1/1")
elif f%2!=0:print(arr[s-n])
else:print(arr[f-s+n-1])