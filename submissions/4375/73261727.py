for i in open(0):
 n,t=int(i),'1'
 while int(t)%n!=0:t+="1"
 print(len(t))