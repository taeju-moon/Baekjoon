import sys
input = sys.stdin.readline

dice = {
    "back": 0,
    "left": 0,
    "up": 0,
    "right": 0,
    "front": 0,
    "bottom": 0
}

# 1. 입력받기
N, M, y, x, K = map(int, input().split())
matrix = [[0] * M for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    for j, data in enumerate(line):
        matrix[i][j] = data

commands = list(map(int, input().split()))


def roll_dice(command):
    global dice
    if command == 1:  # 동

        dice = {
            "back": dice["back"],
            "left": dice["bottom"],
            "up": dice["left"],
            "right": dice["up"],
            "front": dice["front"],
            "bottom": dice["right"]
        }
    elif command == 2:  # 서

        dice = {
            "back": dice["back"],
            "left": dice["up"],
            "up": dice["right"],
            "right": dice["bottom"],
            "front": dice["front"],
            "bottom": dice["left"]
        }

    elif command == 3:  # 북
        dice = {
            "back": dice["up"],
            "left": dice["left"],
            "up": dice["front"],
            "right": dice["right"],
            "front": dice["bottom"],
            "bottom": dice["back"]
        }

    else:  # 남

        dice = {
            "back": dice["bottom"],
            "left": dice["left"],
            "up": dice["back"],
            "right": dice["right"],
            "front": dice["up"],
            "bottom": dice["front"]
        }


# 2. 입력을 하나씩 실행
dy = [0, 0, 0, -1, 1]  # 0, 동, 서, 북, 남
dx = [0, 1, -1, 0, 0]
for command in commands:
    ny = y + dy[command]
    nx = x + dx[command]
    # 주사위는 지도의 바깥으로 이동시킬 수 없다.
    if 0 <= nx < M and 0 <= ny < N:
        # 주사위 굴리기
        roll_dice(command)
        y = ny
        x = nx
        # 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
        if matrix[y][x] == 0:
            matrix[y][x] = dice["bottom"]
        # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
        else:
            dice["bottom"] = matrix[y][x]
            matrix[y][x] = 0
        print(dice["up"])
