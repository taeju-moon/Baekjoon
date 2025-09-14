'''
1. 아이디어
- MSP 기본문제 외우기
- 간선을 인접리스트에 넣기
- 힙에 시작점 넣기
- 힙이 빌때까지 다음의 작업을 반복
    - 힙의 최소값 꺼내서, 해당 노드 방문 안했다면
        - 방문표시, 해당 비용 추가, 연결된 간선들 힙에 넣기
2. 시간복잡도
- MST: O(ELogE)
3. 자료구조
- 인접리스트: [(비용, 노드)[] ]
- 힙: (비용, 노드)[]
- 방문 여부: bool[]
- result: int
'''

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edges = [[] for _ in range(V+1)]
visited = [False] * (V+1)
for _ in range(E):
    start, end, cost = map(int, input().split())
    edges[start].append((cost, end))
    edges[end].append((cost, start))

result = 0
heap = [(0, 1)]
while heap:
    cost, node = heapq.heappop(heap)
    if not visited[node]:
        visited[node] = True
        result += cost
        for edge in edges[node]:
            if not visited[edge[1]]:
                heapq.heappush(heap, edge)

print(result)
