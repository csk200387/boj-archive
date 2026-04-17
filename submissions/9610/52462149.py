ar=[[0,0],[0,0],0]
t=["[1][1]","[0][1]","[0][0]","[1][0]"]
for i in range(int(input())):
    a,b=map(int,input().split())
    if a and b:
        ar[(a>0)][(b>0)]+=1
    else:
        ar[2]+=1
for i in range(4):
    print(f"Q{i+1}: {eval(f'ar{t[i]}')}")
print("AXIS:",ar[2])