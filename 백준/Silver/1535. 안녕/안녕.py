import sys

input = sys.stdin.readline


N = int(input())

L = list(map(int, input().split()))
J = list(map(int, input().split()))
dp = [[0] * 101 for _ in range(N)]

for i in range(N):
    cost = L[i]
    value = J[i]
    for j in range(101):
        if cost >= j:
            if i >= 1:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = 0
        else:
            if i >= 1:
                if j - cost >= 1:
                    dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-cost])
                else:
                    dp[i][j] = max(dp[i-1][j], value)
            else:
                dp[i][j] = value

print(dp[N-1][-1])
