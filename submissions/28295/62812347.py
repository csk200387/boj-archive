r = 0
for i in open(0):
 if int(i)==1:r+=90
 elif int(i)==2:r+=180
 elif int(i)==3:r-=90
print("NESW"[(r%360)//90])