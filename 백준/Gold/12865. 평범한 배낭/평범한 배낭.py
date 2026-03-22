import sys

input = sys.stdin.readline

N, K = map(int, input().split())


w = []
v = []
for _ in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

dp = [[0 for _ in range(K+1)] for _ in range(N)]

for i in range(N):
    weight = w[i]
    value = v[i]
    for k in range(K+1):
        if weight > k:  # 남은 무게가 부족하면 위 칸의 값을 긁어온다.
            if i - 1 >= 0:
                dp[i][k] = dp[i-1][k]
            else:
                dp[i][k] = 0
        else:  # 남은 무게가 넉넉하면 넣기 + dp[i-1][k-weight] 값을 긁어온다.
            if i - 1 >= 0:
                dp[i][k] = max(value + dp[i-1][k-weight], dp[i-1][k])
            else:
                dp[i][k] = value

print(dp[N-1][K])
