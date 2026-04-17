 for i in range(0,int(input())):
  a = input()
  while a.count('(') != 0 and a.count(')') != 0:
      a = a.replace("()","")
  print("YES" if len(a) == 0 else "NO")