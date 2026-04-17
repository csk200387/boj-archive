num, price = map(int, input().split())
res = []
for i in range(num) :
    inp = input()
    res.append(int(inp))
for i in res :
    print(int((i/sum(res))*price))