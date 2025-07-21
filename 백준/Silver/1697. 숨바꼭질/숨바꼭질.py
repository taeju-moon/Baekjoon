'''
1. 아이디어
BFS를 사용하여 현재 갈 수 있는 모든 경로를 Queue에 담아 알맞는 내용을 찾을 때까지 반복한다.
2. 자료구조
Queue: <현재위치, count>
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())


def bfs(s, e):
    # 1. Queue 필요 변수 설정
    queue = []
    visited = [0] * 2000001

    # 2. 초기데이터 삽입
    queue.append((s, 0))
    visited[s] = 1

    while queue:
        data, count = queue.pop(0)
        if data == e:
            return count
        count += 1
        for n in [data-1, data+1, data*2]:
            if 0 <= n < 2000001 and visited[n] == 0:
                queue.append((n, count))
                visited[n] = 1

    return -1


ans = bfs(N, K)
print(ans)
