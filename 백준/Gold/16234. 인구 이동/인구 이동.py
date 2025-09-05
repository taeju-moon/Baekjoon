'''
인구 이동
'''


import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, L, R = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
unions = []  # List<List<(y,x)>>
using_union = []  # List<(y,x)>

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(y, x):
    visited[y][x] = True
    using_union.append((y, x))
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            if L <= abs(matrix[y][x] - matrix[ny][nx]) <= R:
                dfs(ny, nx)


count = 0
while True:
    # 1. 연합을 찾는다.
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j)
                if len(using_union) < 2:
                    using_union = []
                else:
                    unions.append(using_union)
                    using_union = []
    # 2. 찾아낸 연합이 없으면 종료
    if len(unions) == 0:
        break
    # 3. 인구 이동 시작
    for union in unions:  # 모든 연합에 대해
        summed = 0
        for y, x in union:
            summed += matrix[y][x]
        avg = int(summed / len(union))
        for y, x in union:
            matrix[y][x] = avg
    unions = []  # 연합 초기화
    count += 1
    for i in range(N):
        for j in range(N):
            visited[i][j] = False

print(count)
