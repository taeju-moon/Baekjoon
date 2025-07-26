'''
1. 아이디어
- 이중 for문 활용하여 모든 곳을 순회
- visited를 활용하여 갔던 곳 다시 방문 X
- 연결된 내용은 bfs로 찾기

2. 자료구조
- apt_map: int[][]
- visited: bool[][]
- queue
- complex: int[]
'''

N = int(input())
apt_map = [[int(s) for s in input("").replace("\n", "")] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
complex = []

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(a, b):
    count = 1
    queue = [[a, b]]
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            ey = y + dy[i]
            ex = x + dx[i]
            if 0 <= ey < N and 0 <= ex < N:
                if apt_map[ey][ex] == 1 and not visited[ey][ex]:
                    visited[ey][ex] = True
                    count += 1
                    queue.append([ey, ex])
    return count


for i in range(N):
    for j in range(N):
        if apt_map[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            count = bfs(i, j)
            complex.append(count)

complex.sort()
print(len(complex))
for comp in complex:
    print(comp)
