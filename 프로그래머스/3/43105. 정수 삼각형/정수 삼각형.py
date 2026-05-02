def solution(triangle):
    height = len(triangle)
    dp = [[0] * (height+1) for _ in range(height)]
    
    dp[0][0] = triangle[0][0]
    for i in range(1, height):
        for j in range(len(triangle[i])):
            if j >= 1:
                dp[i][j] = max(triangle[i][j] + dp[i-1][j], triangle[i][j] + dp[i-1][j-1])
            else:
                dp[i][j] = triangle[i][j] + dp[i-1][j]

    return max(dp[height-1])