import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())

edges = [[] for _ in range(V+1)]


for _ in range(E):
    start, end, cost = map(int, input().split())
    edges[start].append((cost, end))
    edges[end].append((cost, start))

A, B = map(int, input().split())
heap = [(0, 1)]

distances_from_1 = [INF] * (V+1)
distances_from_1[1] = 0
while heap:
    cost, node = heapq.heappop(heap)
    if distances_from_1[node] != cost:
        continue
    for new_cost, new_node in edges[node]:
        if distances_from_1[new_node] > new_cost + cost:
            distances_from_1[new_node] = new_cost + cost
            heapq.heappush(heap, (distances_from_1[new_node], new_node))

distances_from_A = [INF] * (V+1)
distances_from_A[A] = 0
heap = [(0, A)]
while heap:
    cost, node = heapq.heappop(heap)
    if distances_from_A[node] != cost:
        continue
    for new_cost, new_node in edges[node]:
        if distances_from_A[new_node] > new_cost + cost:
            distances_from_A[new_node] = new_cost + cost
            heapq.heappush(heap, (distances_from_A[new_node], new_node))

distances_from_B = [INF] * (V+1)
distances_from_B[B] = 0
heap = [(0, B)]
while heap:
    cost, node = heapq.heappop(heap)
    if distances_from_B[node] != cost:
        continue
    for new_cost, new_node in edges[node]:
        if distances_from_B[new_node] > new_cost + cost:
            distances_from_B[new_node] = new_cost + cost
            heapq.heappush(heap, (distances_from_B[new_node], new_node))

# case 1 -> A -> B -> N
case1 = INF
if distances_from_1[A] != INF and distances_from_A[B] != INF and distances_from_B[V] != INF:
    case1 = distances_from_1[A] + distances_from_A[B] + distances_from_B[V]
# case 1 -> B -> A -> N
case2 = INF
if distances_from_1[B] != INF and distances_from_B[A] != INF and distances_from_A[V] != INF:
    case2 = distances_from_1[B] + distances_from_B[A] + distances_from_A[V]

result = min(case1, case2)
print(result if result != INF else -1)
