for i in open(0):
 n=int(i)
 t="1"*(len(i)-1)
 while int(t)%n!=0:t+="1"
 print(len(t))