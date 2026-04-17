import sys
input = lambda:sys.stdin.readline().rstrip()
while True:
 n=input()
 if n=="0":break
 r=0
 for c in n:
  if c=="1":r+=2
  elif c=="0":r+=4
  else:r+=3
  r += 1
 print(r+1)