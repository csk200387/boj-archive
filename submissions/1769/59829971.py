t = input()
stack = 0
while len(t) > 1 :
    stack += 1
    t = str(sum(map(int, t)))
print(stack)
print("NO" if int(t)%3>0 else "YES")