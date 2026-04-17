from itertools import *
ran, size = map(int, input().split())
li = list(map(int,input().split()))
for i in sorted(product(li, repeat = size)) :
  print(" ".join(list(map(str,i))))