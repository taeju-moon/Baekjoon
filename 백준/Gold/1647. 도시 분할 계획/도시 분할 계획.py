'''
1. 최소 스패닝 트리로 연결하고 그 중 가장 큰 가중치를 제거
'''

import sys
import heapq
input = sys.stdin.readline


N, M = map(int, input().split())

results = []
edges = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    edges[start].append((cost, end))
    edges[end].append((cost, start))

heap = [(0, 1)]
while heap:
    cost, node = heapq.heappop(heap)
    if not visited[node]:
        visited[node] = True
        results.append(cost)
        for new_cost, new_node in edges[node]:
            if not visited[new_node]:
                heapq.heappush(heap, (new_cost, new_node))

print(sum(results)-max(results))
