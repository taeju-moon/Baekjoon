'''
1. 아이디어
- 2중 for문을 돌면서 값 1 && 방문 X => BFS
- BFS 돌면서 그림 개수 + 1, 최댓값 갱신

2. 시간복잡도
- BFS: O(V+E)
- V: 500 * 500
- E: 4 * 500 * 500
- V+E: 5 * 2500000 = 100만

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문: bool[][]
- Queue(BFS)

'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
map = [list(map(int, input().split())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x):
    rs = 1
    q = [(y, x)]
    while q:
        ey, ex = q.pop(0)
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny, nx))
                    rs += 1
    return rs


cnt = 0
max_size = 0
for j in range(N):
    for i in range(M):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 1. 전체 그림 개수를 + 1
            cnt += 1
            # 2. BFS > 그림 크기를 구해주고
            max_size = max(max_size, bfs(j, i))
            # 3. 그림 최대 크기 갱신

print(cnt)
print(max_size)
