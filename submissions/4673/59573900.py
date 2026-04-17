s = set(range(1,10001))
res = {sum(map(int,list(str(i))))+i for i in range(1,10001)}
print(*sorted(s-res))