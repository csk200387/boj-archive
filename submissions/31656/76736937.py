c = input()
r = [c[0]]
for i in c[1:]:
  if r[-1] != i:
    r.append(i)
print("".join(r))