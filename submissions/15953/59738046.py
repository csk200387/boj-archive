A = [5000000] + [3000000]*2 + [2000000]*3 + [500000]*4 + [300000]*5 + [100000]*6
B = [5120000] + [2560000]*2 + [1280000]*4 + [640000]*8 + [320000]*16

for i in range(int(input())) :
    a, b = map(int, input().split())
    price = 0
    if a <= 21 :
        price += A[a-1]
    else :
        price += 0
    if b <= 31 :
        price += B[b-1]
    else :
        price += 0
    print(price)