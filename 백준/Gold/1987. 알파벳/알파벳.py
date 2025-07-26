'''
1. 아이디어
- DFS를 이용하여 모든 지나온 알파벳들을 계속 넘기며 최댓값을 구한다.
- 리프 노드 (더이상 갈 수 없는 상황)이 나왔을때 최댓값을 계속해서 기록한다.
2. 자료구조
- mapped_data: int[][]
- visited: Node<y,x>[]
'''

import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(100000)

R, C = map(int, input().split())
mapped_data = [[s for s in input().strip()] for _ in range(R)]

visited = {}

result = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(y, x, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and not visited.get(mapped_data[ny][nx]):
            visited[mapped_data[ny][nx]] = True
            dfs(ny, nx, cnt+1)
            visited[mapped_data[ny][nx]] = False


visited[mapped_data[0][0]] = True
dfs(0, 0, 1)

print(result)
