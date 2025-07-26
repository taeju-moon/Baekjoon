'''
1. 아이디어
- 각 테스트 케이스에서 DFS를 통해 섬의 개수를 센다. 

2. 자료구조

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


dy = [0, 1, 0, -1, 1, 1, -1, -1]
dx = [1, 0, -1, 0, 1, -1, -1, 1]


def dfs(y, x, matrix, visited, N, M):
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < M and 0 <= ny < N:
            if matrix[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx, matrix, visited, N, M)


result = []

while True:
    M, N = map(int, input().split())
    if N == 0 and M == 0:
        break
    mapped_data = [[int(s) for s in input().split()] for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if mapped_data[i][j] == 1 and not visited[i][j]:
                cnt += 1
                dfs(i, j, mapped_data, visited, N, M)
    result.append(cnt)

for cnt in result:
    print(cnt)
