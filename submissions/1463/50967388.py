n = int(input())
stack = 0
while True :
  if n == 1 :
    print(stack)
    break
  elif (n-1) % 3 == 0 :
    n -= 1
  elif n % 3 == 0 :
    n = n//3
  elif n % 2 == 0 :
    n = n//2
  else :
    n -= 1
  stack += 1