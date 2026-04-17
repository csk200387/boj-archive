size = int(input())
potatos = sorted(map(int, input().split()), reverse=True)
tmp = potatos[:size//2+1]
sangwoo = sum(tmp)
park = sum(potatos)-sum(tmp)
print(park, sangwoo)