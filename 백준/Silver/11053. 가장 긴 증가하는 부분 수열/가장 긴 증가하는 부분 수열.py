import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N+1)  # dp[i] <- i번째 숫자 추가시 얻을 수 있는 최대 길이

for i in range(1, N+1, 1):
    result = 0
    data = arr[i]
    for j in range(0, i):
        if arr[j] < arr[i]:
            result = max(result, dp[j])
    dp[i] = result + 1

print(max(dp))
