n,*arr=open(0)
for i in arr:
 a,b,c,d=map(int,i.split())
 if (t:=a*b)==(e:=c*d):print("Tie")
 else:print(["Eurecom","TelecomParisTech"][t>e])