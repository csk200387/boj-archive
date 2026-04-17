m, e = [], []
for _ in range(4) :
    m.append(int(input()))
for _ in range(2) :
    e.append(int(input()))
print(sum(m)-min(m)+max(e))