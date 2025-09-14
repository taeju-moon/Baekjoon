import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, input().split())
go_distances = [INF] * (N+1)
back_distances = [INF] * (N+1)
edges = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    edges[start].append((cost, end))


# 1. 집에서 파티로 가는 데에 드는 시간
for i in range(1, N+1):  # 모든 학생들에 대해서 다익스트라 실행
    if i == X:
        go_distances[i] = 0
        continue
    distances = [INF] * (N+1)
    distances[i] = 0
    heap = [(0, i)]
    while heap:
        cost, node = heapq.heappop(heap)
        if distances[node] != cost:
            continue
        for new_cost, new_node in edges[node]:
            if distances[new_node] > new_cost + cost:
                distances[new_node] = new_cost + cost
                heapq.heappush(heap, (distances[new_node], new_node))
    go_distances[i] = distances[X]

heap = [(0, X)]  # (비용, 노드)
back_distances[X] = 0
# 2. 파티 끝나고 집으로 가는 데에 드는 시간
while heap:
    cost, node = heapq.heappop(heap)
    # 갔던 항목 제거
    if back_distances[node] != cost:
        continue
    for new_cost, new_node in edges[node]:
        if back_distances[new_node] > cost + new_cost:
            back_distances[new_node] = cost + new_cost
            heapq.heappush(heap, (back_distances[new_node], new_node))

max_num = 0
for i in range(1, N+1, 1):
    a = go_distances[i]
    b = back_distances[i]
    max_num = max(a+b, max_num)

print(max_num)
