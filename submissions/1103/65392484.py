size = int(input())
potatos = sorted(map(int, input().split()))
tmp = potatos[:size//2]
park = sum(tmp)
sangwoo = sum(potatos)-sum(tmp)
print(park, sangwoo)