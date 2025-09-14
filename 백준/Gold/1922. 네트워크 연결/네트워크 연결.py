'''
1. 아이디어
- 최소 스패닝 트리
    - 힙에서 내용물을 빼면서 not visited시에
        - 방문 처리, 전체 값에 더하기, 방문하지 않은 노드를 갈 수 있는지 찾아봐서 힙에 담기
2. 자료구조
- edges: [(비용, 노드)[] ... ]
- visited: bool[]
- heap: (비용, 노드)[]
'''

import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

edges = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    edges[start].append((cost, end))
    edges[end].append((cost, start))

heap = [(0, 1)]

result = 0
while heap:
    cost, node = heapq.heappop(heap)
    if not visited[node]:
        visited[node] = True
        result += cost
        for new_cost, new_node in edges[node]:
            if not visited[new_node]:
                heapq.heappush(heap, (new_cost, new_node))

print(result)
