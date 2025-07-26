'''
1. 아이디어
- 노드의 연결정보를 저장한다.
- DFS를 통해 모든 노드를 순회하면서 부모 노드의 정보를 하위로 넘기며 해당 그 정보를 기록한다.
2. 자료구조
- result: int[] 각 노드의 부모 노드를 정리한 결과값
- tree_map: int[ int[] ] 
- visited: bool[] 노드의 방문 여부
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


N = int(input())
result = [0] * (N+1)
tree_map = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    tree_map[a].append(b)
    tree_map[b].append(a)


def dfs(node, parent):
    visited[node] = True
    result[node] = parent
    for child in tree_map[node]:
        if not visited[child]:
            dfs(child, node)


dfs(1, 0)

for i in range(2, N+1, 1):
    print(result[i])
