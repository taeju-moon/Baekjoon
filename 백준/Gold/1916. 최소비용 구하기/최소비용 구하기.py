'''
1. 아이디어
- 다익스트라 사용
2. 자료구조
- 거리배열: int[] <- INF로 초기화
- heap: (비용, 노드)[]
- 노드 인접리스트: (비용, 노드)[] edges
'''

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

# 1. 입력값 받기
N = int(input())
M = int(input())
edges = [[] for _ in range(N+1)]  # 정점의 개수 + 1
distances = [INF] * (N+1)

for _ in range(M):
    start, end, cost = map(int, input().split())
    edges[start].append((cost, end))

start, end = map(int, input().split())

# 2. 거리 및 힙 초기화
distances[start] = 0
heap = [(0, start)]

while heap:
    cost, node = heapq.heappop(heap)
    # 1. 겹치는지 확인
    if distances[node] != cost:
        continue
    # 2. 갈 수 있는 정점들에 대해서 경로의 최소값일 때 distance 갱신 및 heap에 넣기
    for edge_cost, edge_node in edges[node]:
        if distances[edge_node] > edge_cost + cost:
            distances[edge_node] = edge_cost + cost
            heapq.heappush(heap, (distances[edge_node], edge_node))

print(distances[end])
