for line in open(0):
 a,b,c=map(int,line.split())
 print(max(b-a-1,c-b-1))