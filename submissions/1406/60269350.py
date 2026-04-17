r,_,*C=open(0)
r,l=[*r[:-1]],[]
for c in C:
 if c=='L\n':
  if r:l.append(r.pop())
 elif c == 'D\n':
  if l:r.append(l.pop())
 elif c == 'B\n':
  if r:r.pop()
 else:r.append(c[2])
print(''.join(r + l[::-1]))