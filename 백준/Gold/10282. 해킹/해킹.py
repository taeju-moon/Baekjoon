import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())

results = []
for _ in range(N):
    n, d, c = map(int, input().split())

    adj_list = [[] for _ in range(n+1)] #(cost, b)

    for _ in range(d):
        a, b, cost = map(int, input().split())
        adj_list[b].append((cost, a))

    queue = deque()
    queue.append((0, c))

    distances = [INF] * (n+1)
    distances[c] = 0

    while queue:
        cost, node = queue.popleft()
        for new_cost, new_node in adj_list[node]:
            if distances[new_node] > cost + new_cost:
                distances[new_node] = cost + new_cost
                queue.append((cost+new_cost, new_node))

    infected = list(filter(lambda x: x != INF, distances))
    result = (len(infected), max(infected) if len(infected) != 0 else 0)
    results.append(result)

for result in results:
    print(result[0], result[1])