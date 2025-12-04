import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

N, K = map(int, input().split())

distances = [INF] * 100001

queue = deque()  # (cost, node)[]
queue.append((0, N))
distances[N] = 0

isFound = False
min_cost = INF
found_num = 0
while queue:

    cost, node = queue.popleft()

    if isFound and cost > min_cost:
        continue

    if distances[node] < cost:
        continue

    if node == K:
        isFound = True
        min_cost = cost
        found_num += 1
        continue

    for new_cost, new_node in [(1, node+1), (1, node-1), (1, node * 2)]:
        if 0 <= new_node <= 100000:
            if distances[new_node] >= cost + new_cost:
                distances[new_node] = cost + new_cost
                queue.append((cost + new_cost, new_node))


print(min_cost)
print(found_num)
