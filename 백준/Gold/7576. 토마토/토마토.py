'''
<시간초과>
1. 아이디어
- 하루마다 이를 반복한다.
- 토마토가 모두 잘 익었는지 확인한다.
- 전날 queue에 익은 토마토를 전부 집어넣는다.
- queue.pop() 하면서 익은 토마토 주위의 토마토를 전부 익게 만들며 queue에 넣는다.
- queue가 사라질때까지 반복한다.
2. 자료구조
- tomatos: int[][]
- queue: Node<y, x>[]
- count: int(몇일차)
'''

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
count = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

need_to_ripe = M * N


def check_tomatos():
    global need_to_ripe
    return need_to_ripe == 0


def get_initial_queue():
    global need_to_ripe
    queue = []
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 1 or tomatos[i][j] == -1:
                need_to_ripe -= 1
            if tomatos[i][j] == 1:
                queue.append([i, j])
    return queue


def process():
    global count
    global need_to_ripe

    queue = get_initial_queue()

    while queue:
        if check_tomatos():
            break
        else:
            count += 1
            new_queue = []
            for data in queue:
                y, x = data
                for i in range(4):
                    ey = y + dy[i]
                    ex = x + dx[i]
                    if 0 <= ey < N and 0 <= ex < M:
                        if tomatos[ey][ex] == 0:
                            tomatos[ey][ex] = 1
                            new_queue.append([ey, ex])
                            need_to_ripe -= 1

            queue = new_queue

    if check_tomatos():
        print(count)
    else:
        print(-1)


process()
