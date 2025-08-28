import sys
from collections import deque
input = sys.stdin.readline


times = int(input())
result = []

for _ in range(times):
    N, M = map(int, input().split())

    queue = deque(map(lambda x: [int(x), False], input().split()))
    queue[M][1] = True

    count = 0
    while queue:
        data, isObject = queue.popleft()
        # 뽑은 데이터가 우선순위가 가장 높을 경우
        if not queue or data >= max(map(lambda x: x[0], queue)):
            count += 1
            if isObject:
                break
        # 뽑은 데이터의 우선순위가 밀릴 경우
        else:
            queue.append([data, isObject])

    result.append(count)

for r in result:
    print(r)
