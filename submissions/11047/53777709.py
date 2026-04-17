n, money = map(int, input().split())
coins = []
for i in range(n) :
    coins.append(int(input()))
for i in range(n-1, -1, -1) :
    t = money//coins[i]
    money -= coins[i]*t
    coins[i] = t
print(sum(coins))