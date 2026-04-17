input()
a = [*map(int, input().split())]
t = sum(a, start=(len(a)-1)*8)
print(t//24, t%24)