import sys
input = sys.stdin.readline

N = int(input())
matrix = [[0] * (N+1) for _ in range(N+1)]
dp = [[0] * (N+1) for _ in range(N+1)]

# matrix 초기화
for i in range(1, N+1):
    datas = list(map(int, input().split()))
    for j in range(1, i+1):
        matrix[i][j] = datas[j-1]

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i][j] = matrix[i][j] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[N]))
