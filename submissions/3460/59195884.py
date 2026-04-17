for _ in range(int(input())) :
 for i,x in enumerate(str(bin(int(input())))[::-1]) :
  if x == "1" :
   print(i, end=" ")