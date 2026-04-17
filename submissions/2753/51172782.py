y = int(input())
if y%4 == 0 :
  if y%500 != 0 and y%100 == 0 :
    print(0)
  else :
    print(1)
else :
  print(0)