'''
1. 아이디어
- 첫번째 노드로부터 BFS 실행
- 다음 노드로 지금까지 밟고 간 노드의 개수 정보 삽입

2. 자료구조
- map: int[][]
- chk: bool[][]
- queue: Node<y, x, cnt>[]

'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

target_y = N-1
target_x = M-1

map = [[int(s) for s in input().replace("\n", "")] for _ in range(N)]
chk = [[False] * M for _ in range(N)]


# 기본값 처리
queue = [[0, 0, 1]]
chk[0][0] = True
result = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


while queue:
    y, x, cnt = queue.pop(0)
    if y == target_y and x == target_x:
        result = cnt
        break
    for i in range(4):
        ey = y + dy[i]
        ex = x + dx[i]
        if 0 <= ey <= target_y and 0 <= ex <= target_x:
            if chk[ey][ex] == False and map[ey][ex] == 1:
                chk[ey][ex] = True
                queue.append([ey, ex, cnt+1])


print(result)
