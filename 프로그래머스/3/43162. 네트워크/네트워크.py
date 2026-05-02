from collections import deque
cnt = 0
visited = []

def bfs(n, node, computers):
    global visited
    queue = deque()
    queue.append(node)
    
    while queue:
        elem = queue.popleft()
        visited[elem] = True
        for i in range(n):
            if not visited[i] and computers[elem][i]:
                queue.append(i)

def solution(n, computers):
    global cnt
    global visited 
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(n, i, computers)
            cnt +=1
            print(visited)
    return cnt
