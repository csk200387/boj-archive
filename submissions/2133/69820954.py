dp = [0] * 31
dp[2] = 3
for i in range(3, 31):
    if i % 2 == 1:
        continue
    dp[i] = 4*dp[i-2]
print(dp[int(input())])