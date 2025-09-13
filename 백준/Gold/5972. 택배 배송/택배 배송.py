'''
1. 아이디어
- 다익스트라
2. 자료구조
- heap: (비용, 노드)[]
- distances: int[]
- edges: (비용, 노드)[] , 인접리스트
'''

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

# 1. 입력받기
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
distances = [INF] * (N+1)

for i in range(M):
    start, end, cost = map(int, input().split())
    edges[start].append((cost, end))
    edges[end].append((cost, start))

# 2. 기본값 세팅
distances[1] = 0
heap = [(0, 1)]  # (비용, 노드)

# 3. 다익스트라 순회
while heap:
    cost, node = heapq.heappop(heap)
    # 중복 제거
    if distances[node] != cost:
        continue

    for new_cost, new_node in edges[node]:
        if distances[new_node] > cost + new_cost:
            distances[new_node] = cost + new_cost
            heapq.heappush(heap, (distances[new_node], new_node))

print(distances[N])
