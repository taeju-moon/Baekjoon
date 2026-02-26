import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())

matrix = [ [int(d) for d in input().strip("\n")] for _ in range(M)]
costs = [ [INF] * N for _ in range(M)]
visited = [ [False] * N for _ in range(M)]

dy = [1,0,-1,0]
dx = [0,1,0,-1]

queue = [(0, 0, 0)] #(cost, y, x)
costs[0][0] = 0

while queue:
    cost, y, x = heapq.heappop(queue)
    visited[y][x] = True

    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0 <= new_y < M and 0 <= new_x < N:
            if not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                new_cost = cost + (1 if matrix[new_y][new_x] else 0)
                if costs[new_y][new_x] > new_cost:
                    costs[new_y][new_x] = new_cost
                    heapq.heappush(queue, (new_cost, new_y, new_x))

print(costs[-1][-1])