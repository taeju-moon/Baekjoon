from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

queue = deque()  # (cost, node)
queue.append((1, N))

found = False
while queue:
    cost, node = queue.popleft()

    if node == M:
        print(cost)
        found = True
        break

    if node > M:
        continue

    queue.append((cost+1, node*2))
    queue.append((cost+1, int(str(node)+"1")))

if not found:
    print(-1)
