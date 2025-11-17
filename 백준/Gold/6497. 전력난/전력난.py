import sys
import heapq

input = sys.stdin.readline

while True:
    M, N = map(int, input().split())
    if M == N == 0:
        break
    visited = [False] * M
    edges = [[] for _ in range(M)]  # (cost, node)
    total_cost = 0

    for _ in range(N):
        a, b, cost = map(int, input().split())
        total_cost += cost

        edges[a].append((cost, b))
        edges[b].append((cost, a))

    used_cost = 0
    queue = [(0, 0)]  # (cost, node)
    while queue:
        cost, node = heapq.heappop(queue)
        if not visited[node]:
            visited[node] = True
            used_cost += cost
            for cost2, node2 in edges[node]:
                if not visited[node2]:
                    heapq.heappush(queue, (cost2, node2))

    print(total_cost - used_cost)
