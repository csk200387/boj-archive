L, D, X = map(int, open(0))
t = [i for i in range(L, D+1) if sum(map(int, str(i))) == X]
print(min(t))
print(max(t))