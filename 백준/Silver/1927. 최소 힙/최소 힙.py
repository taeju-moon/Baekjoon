import heapq
import sys
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    data = int(input())
    if data != 0:
        heapq.heappush(queue, data)
        continue

    if queue:
        print(heapq.heappop(queue))
    else:
        print(0)
