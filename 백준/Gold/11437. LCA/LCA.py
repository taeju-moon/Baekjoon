import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
edges = [[] for _ in range(N+1)]
depths = [0] * (N+1)
visited = [False] * (N+1)
parent = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(node, depth):
    if visited[node]:
        return
    visited[node] = True
    depths[node] = depth
    for next_node in edges[node]:
        if parent[next_node] == 0:
            parent[next_node] = node
            dfs(next_node, depth+1)


dfs(1, 0)

results = []
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    # 1. depth를 알맞게 맞추기
    while depths[a] != depths[b]:
        if depths[a] > depths[b]:
            a = parent[a]
        else:
            b = parent[b]
    # # a와 b가 완전히 똑같아 질때까지 a와 b를 계속 위로 올리기
    while a != b:
        a = parent[a]
        b = parent[b]

    results.append(a)

for result in results:
    print(result)
