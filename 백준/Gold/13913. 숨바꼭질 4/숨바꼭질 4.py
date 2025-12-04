import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

a, b = map(int, input().split())


heap = [(0, a)]  # (cost, node)
visited = [False] * 100001
distances = [INF] * 100001
parents = [0] * 1000001
visited[a] = True
distances[a] = 0
parents[a] = a

while heap:
    cost, node = heapq.heappop(heap)

    if node == b:
        print(cost)
        path = [node]
        while parents[node] != node:
            path.append(parents[node])
            node = parents[node]
        path.reverse()
        for p in path:
            print(p, end=" ")
        break

    if distances[node] < cost:
        continue

    for c, next_node in [(cost+1, node + 1), (cost + 1, node-1), (cost+1, node * 2)]:
        if 0 <= next_node <= 100000:

            if c < distances[next_node]:
                distances[next_node] = c
                parents[next_node] = node
                heapq.heappush(heap, (c, next_node))
