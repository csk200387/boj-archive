num = int(input())
for i in range(0,num):
  a = input()
  while a.count('(') != 0 and a.count(')') != 0:
      a = a.replace("()","")
  if len(a) == 0:
    print("YES")
  else:
    print("NO")