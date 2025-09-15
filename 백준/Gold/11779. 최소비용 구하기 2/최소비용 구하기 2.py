import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

edges = [[] for _ in range(N+1)]
distances = [[INF, []] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    edges[start].append((cost, end))

start, end = map(int, input().split())
heap = [[0, start]]
distances[start][0] = 0  # 시작점 0으로 초기화
distances[start][1] = [start]  # 시작점에서 지나친 리스트 초기화

while heap:
    cost, node = heapq.heappop(heap)
    if distances[node][0] != cost:
        continue
    for new_cost, new_node in edges[node]:
        if distances[new_node][0] > new_cost + cost:
            distances[new_node][0] = new_cost + cost
            distances[new_node][1] = [data for data in distances[node][1]]
            distances[new_node][1].append(new_node)
            heapq.heappush(heap, [distances[new_node][0], new_node])


print(distances[end][0])
print(len(distances[end][1]))
for path in distances[end][1]:
    print(path, end=" ")
