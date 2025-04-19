N, M, V = map(int, input().split())

def dfs(node, visited, graph):
    print(node, end=' ')
    visited[node] = True
    for i in range(1,N+1):
        if not visited[i] and graph[node][i]:
            dfs(i, visited, graph)

def bfs(queue, visited, graph):
    while queue:
        data = queue.pop(0)
        print(data, end=' ')
        for i in range(1,N+1):
            if not visited[i] and graph[data][i]:
                queue.append(i)
                visited[i] = True

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


#dfs
dfs(V, visited, graph)
print()

#bfs
visited = [False] * (N+1)
queue = [V]
visited[V] = True
bfs(queue, visited, graph)