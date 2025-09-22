

dp = [0] * 46
dp[0] = 0
dp[1] = 1
dp[2]

for i in range(2, 46, 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[int(input())])
