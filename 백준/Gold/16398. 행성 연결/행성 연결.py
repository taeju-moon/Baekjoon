import sys
import heapq

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
queue = [(0, 0)]

costs = 0

while queue:
    cost, node = heapq.heappop(queue)
    if visited[node]:
        continue

    costs += cost
    visited[node] = True

    for i in range(N):
        if not visited[i]:
            heapq.heappush(queue, (matrix[node][i], i))


print(costs)
