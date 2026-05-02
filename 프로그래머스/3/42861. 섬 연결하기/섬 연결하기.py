import heapq

def solution(n, costs):
    edges = {} # from: (to, cost)
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        edges[i] = []
    for start, end, cost in costs:
        edges[start].append((end, cost))
        edges[end].append((start, cost))
        
    queue = [(0, 0)] #(cost, node)
    while queue:
        cost, node = heapq.heappop(queue)
        if visited[node]:
            continue
        
        visited[node] = True
        answer += cost
        
        for next_node, next_cost in edges[node]:
            if not visited[next_node]:
                heapq.heappush(queue, (next_cost, next_node))
                
    return answer