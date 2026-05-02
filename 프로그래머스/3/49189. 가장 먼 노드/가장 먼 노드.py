from collections import deque
import sys

INF = sys.maxsize

def solution(n, edge):
    distances = [INF] * (n+1)
    distances[0] = 0
    distances[1] = 0
    visited = [False] * (n+1)
    
    queue = deque() #(cost, node)
    queue.append((0, 1))
    
    graph = {}
    for a,b in edge:
        if graph.get(a):
            graph[a].append(b)
        else:
            graph[a] = [b]
        if graph.get(b):
            graph[b].append(a)
        else:
            graph[b] = [a]
    
    while queue:
        cost, node = queue.popleft()
        visited[node] = True
        distances[node] = min(distances[node], cost)
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((cost+1, next_node))
                
    max_d = max(distances)
    answer = 0
    for distance in distances:
        if distance == max_d:
            answer +=1
    return answer