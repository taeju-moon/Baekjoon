'''
a. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
b. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
c. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
d. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
'''
import sys
from collections import deque
input = sys.stdin.readline


# 1. 보드 초기화 (0: 비어있음, 1: 사과, 2: 뱀)
N = int(input())
board = [[0] * (N) for _ in range(N)]

# 2. 보드에 사과를 놓기(1)
K = int(input())
for _ in range(K):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

# 3. 뱀을 이동시킬 경로 담기
L = int(input())
tracks = deque()
for _ in range(L):
    a, b = input().split()
    tracks.append((int(a), b))

# 4. 실제로 뱀을 이동시키기
snake = deque()
snake.appendleft((0, 0))
board[0][0] = 2
x = 0
y = 0
second = 0

# 위치정보: 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

second = 0
while True:
    second += 1
    # 다음에 이동할 경로
    nx = snake[0][0] + dx[direction]
    ny = snake[0][1] + dy[direction]
    # b. 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
    if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
        break

    # a. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    snake.appendleft((nx, ny))

    # c. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[nx][ny] == 1:
        pass
    # d. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else:
        x, y = snake.pop()
        board[x][y] = 0

    board[nx][ny] = 2
    # 뱀의 방향 변환 정보 반영
    if tracks and tracks[0][0] == second:
        sec, dir = tracks.popleft()
        if dir == "L":
            direction = (direction + 4 - 1) % 4
        else:
            direction = (direction + 4 + 1) % 4


print(second)
