str = input()
ar = []
for i in range(len(str)):
    t = len(str)-len(str[:i+1])
    ar.append((t,str[:i+1]))
ar.sort(key=lambda x:x[1], reverse=True)
t = [x[0] for x in ar]
print(*t)