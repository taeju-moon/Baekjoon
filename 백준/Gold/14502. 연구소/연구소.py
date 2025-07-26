'''
1. 아이디어
- possible_walls_point: 벽을 세울 수 있는 모든 포인트들을 체크
- possible_walls_point를 3개씩 조합해 모든 경우의 수 찾기
- 모든 경우의 수에 대해서 각각 bfs를 돌려서 안전 영역의 최대 경우의 수 찾기

2. 자료구조

mapped_data: int[][]

'''
from itertools import combinations
from collections import deque
import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
mapped_data = [[int(s) for s in input().split()] for _ in range(N)]

possible_walls_point = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

result = 0


def bfs(matrix):
    queue = deque()

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                queue.append((i, j))

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ey = y + dy[i]
            ex = x + dx[i]
            if 0 <= ey < N and 0 <= ex < M:
                if matrix[ey][ex] == 0:
                    matrix[ey][ex] = 2
                    queue.append((ey, ex))

    global result
    temp = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                temp += 1

    result = max(result, temp)


for i in range(N):
    for j in range(M):
        data = mapped_data[i][j]
        if data == 0:
            possible_walls_point.append((i, j))

for c in combinations(possible_walls_point, 3):
    copied_mapped_data = copy.deepcopy(mapped_data)
    for y, x in c:
        copied_mapped_data[y][x] = 1

    bfs(copied_mapped_data)

print(result)
