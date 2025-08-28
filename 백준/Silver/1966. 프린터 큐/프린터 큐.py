import sys
from collections import deque
input = sys.stdin.readline


times = int(input())
result = []

for _ in range(times):
    N, M = map(int, input().split())

    priorities = list(map(int, input().split()))
    queue = deque(map(lambda x: [int(x), False], priorities))
    queue[M][1] = True
    priorities.sort(reverse=True)

    count = 0
    while queue:
        data, isObject = queue.popleft()
        # 뽑은 데이터가 우선순위가 가장 높을 경우
        if not queue or data >= priorities[0]:
            priorities.pop(0)
            count += 1
            if isObject:
                break
        # 뽑은 데이터의 우선순위가 밀릴 경우
        else:
            queue.append([data, isObject])

    result.append(count)

for r in result:
    print(r)
