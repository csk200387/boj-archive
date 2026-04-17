r = 0
for i in open(0):
 if int(i)==1:r+=90
 elif int(i)==2:r+=180
 elif int(i)==3:r-=90
r%=360

if r == 0:
 print('N')
elif r == 90:
 print('E')
elif r == 180:
 print('S')
elif r == 270:
 print('W')