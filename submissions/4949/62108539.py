for l in [*open(0)][:-1]:
 s=[]
 for i in l:
  if i in'([])':s.append(i)
  if s[-2:]==list('()'):s.pop();s.pop()
  elif s[-2:]==list('[]'):s.pop();s.pop()
 print('yes'if not s else'no')