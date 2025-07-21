'''
1. 아이디어
- graph 대상 이중 for문을 돌면서
- Queue에 칠해진 내용으로 bfs를 돌려서 연결된 컴포넌트를 확인한다.
- visited로써 중복 체크 진행한다.
2. 자료구조 -> 행렬에서 연결리스트로 변경
graph: int[N+1][N+1]
visited: int[N+1][N+1]
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(data):
    visited[data] = True
    for to in graph[data]:
        if not visited[to]:
            dfs(to)


for i in range(1, N+1, 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
