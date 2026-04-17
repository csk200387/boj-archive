table = [[False]*100 for _ in range(100)]
for data in open(0) :
    ldx, ldy, rux, ruy = map(int, data.split())
    for i in range(ldy, ruy) :
        for l in range(ldx, rux) :
            table[i][l] = True
print(sum(table, []).count(True))