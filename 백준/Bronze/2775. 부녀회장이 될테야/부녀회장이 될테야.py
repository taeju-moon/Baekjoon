import sys
input = sys.stdin.readline

# 층: 행, 호: 열
dp = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15):
    dp[0][i] = i

for i in range(1, 15):
    for j in range(15):
        dp[i][j] = sum(dp[i-1][:j+1])

results = []
N = int(input())
for _ in range(N):
    k = int(input())
    n = int(input())
    results.append(dp[k][n])

for result in results:
    print(result)
