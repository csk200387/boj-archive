data = input()
s = set(data)
for i in range(len(data)):
    for l in range(1, len(data)-i+1):
        s.add(data[i:i+l])
print(len(s))