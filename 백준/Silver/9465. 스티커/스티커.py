import sys

input = sys.stdin.readline

T = int(input())

results = []

for _ in range(T):
    N = int(input())
    scores = []
    dp = [[0] * N for _ in range(2)]
    for i in range(2):
        row = list(map(int, input().strip("\n").split()))
        scores.append(row)

    if N == 1:
        results.append(max(scores[0][0], scores[1][0]))
    elif N == 2:
        results.append(max(scores[0][0] + scores[1]
                       [1], scores[0][1] + scores[1][0]))
    else:
        dp[0][0] = scores[0][0]
        dp[1][0] = scores[1][0]
        dp[0][1] = scores[1][0] + scores[0][1]
        dp[1][1] = scores[0][0] + scores[1][1]
        for j in range(2, N, 1):
            dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + scores[0][j]
            dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + scores[1][j]
        results.append(max(dp[0][N-1], dp[1][N-1]))

for result in results:
    print(result)
