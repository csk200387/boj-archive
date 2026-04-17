n,*a=open(0)
for i in a:
 a,b,c,d=map(int,i.split())
 print(["Eurecom","TelecomParisTech"][a*b>c*d])