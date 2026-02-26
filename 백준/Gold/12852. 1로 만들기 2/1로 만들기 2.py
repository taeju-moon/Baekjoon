import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
N = int(input())

dp = [0] * 1000001
parents = [0] * 1000001
dp[1] = 0

for i in range(2,1000001):
    c1 = INF
    c2 = INF
    c3 = INF
    if i % 3 == 0:
        c3 = dp[int(i/3)] + 1
    if i % 2 == 0:
        c2 = dp[int(i/2)] + 1
    c1 = dp[i-1] +1
    
    candidates = [c1, c2, c3]
    dp[i] = min(c1, c2, c3)
    parent =  candidates.index(dp[i])

    if parent == 0:
        parents[i] = i-1
    elif parent == 1:
        parents[i] = int(i / 2)
    else:
        parents[i] = int(i/3)
    

print(dp[N])

current = N
while current != 1:
    print(current, end=" ")
    current = parents[current]
print(1, end=" ")