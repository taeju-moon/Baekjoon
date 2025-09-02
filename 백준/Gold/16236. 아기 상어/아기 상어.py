import sys
from collections import deque

input = sys.stdin.readline


def find_fish(start, size, matrix):
    queue = deque([start])
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    fish_list = []
    fish_flag = False

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    while queue:
        y, x, count = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                # 물고기가 상어보다 클때
                if matrix[ny][nx] and size < matrix[ny][nx]:
                    continue
                # 상어가 물고기보다 클때
                elif matrix[ny][nx] and size > matrix[ny][nx]:
                    fish_list.append((ny, nx, count+1))
                    visited[ny][nx] = True
                    fish_flag = True
                # 물고기가 없거나 상어와 물고기가 같을때
                else:
                    visited[ny][nx] = True
                    queue.append((ny, nx, count+1))

    return (fish_flag, fish_list)


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

start = [0, 0, 0]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            start = [i, j, 0]
            matrix[i][j] = 0

second, fish_count, size = 0, 0, 2

while True:
    flag, fish_result = find_fish(start, size, matrix)
    if flag:
        # 먹을 수 있는 물고기 정렬 > 가까운 위치 / 행 / 열
        fish_result = sorted(fish_result, key=lambda x: (x[2], x[0], x[1]))

        fish = fish_result[0]
        second += fish[2]
        fish_count += 1
        if fish_count == size:
            size += 1
            fish_count = 0
        matrix[fish[0]][fish[1]] = 0
        start = [fish[0], fish[1], 0]
    else:
        break

print(second)
