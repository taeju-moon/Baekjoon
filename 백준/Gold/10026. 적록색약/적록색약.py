'''
1. 아이디어
- 적록색약이 있는 내용에 대해서
- 정상인에 대해서
- 따로따로 BFS를 돌린다

'''

import sys
input = sys.stdin.readline

N = int(input())
color_map = [[s for s in input().replace("\n", "")] for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x):
    queue = [(y, x)]
    while queue:
        y, x = queue.pop(0)
        visited[y][x] = True
        data = color_map[y][x]
        for i in range(4):
            ey = y + dy[i]
            ex = x + dx[i]
            if 0 <= ey < N and 0 <= ex < N:
                if not visited[ey][ex] and data == color_map[ey][ex]:
                    visited[ey][ex] = True
                    queue.append((ey, ex))


normal_count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            normal_count += 1
            bfs(i, j)

color_blind_count = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if color_map[i][j] == "R":
            color_map[i][j] = "G"

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color_blind_count += 1
            bfs(i, j)

print(f"{normal_count} {color_blind_count}")
