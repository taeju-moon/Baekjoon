import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# adj_list 0: (node, distance)
adj_list = [[] for _ in range(N+1)]


for _ in range(N-1):
    a, b, cost = map(int, input().split())
    adj_list[a].append((b, cost))
    adj_list[b].append((a,cost))

results = []
for _ in range(M):
    a, b = map(int, input().split())
    visited = [False] * (N+1)
    queue = deque() # (node, cost)
    queue.append((a,0))
    while queue:
        node, cost = queue.popleft()
        visited[node] = True
        for next_node, next_cost in adj_list[node]:
            if next_node == b:
                results.append(cost+next_cost)
                break
            if not visited[next_node]:
                queue.append((next_node, cost + next_cost))

for result in results:
    print(result)