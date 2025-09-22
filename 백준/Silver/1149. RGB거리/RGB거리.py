import sys
input = sys.stdin.readline

N = int(input())

dp = [[0, 0, 0] for _ in range(N+1)]  # (이 집이 R,G,B 였을때의 최소값)[]

for i in range(1, N+1, 1):
    r, g, b = map(int, input().split())
    # r
    dp[i][0] = r + min(dp[i-1][1], dp[i-1][2])
    # g
    dp[i][1] = g + min(dp[i-1][0], dp[i-1][2])
    # b
    dp[i][2] = b + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N]))
