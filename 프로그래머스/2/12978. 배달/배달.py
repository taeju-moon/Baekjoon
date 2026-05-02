import heapq
import sys
INF = sys.maxsize

def solution(N, road, K):
    edges = {}
    for i in range(1, N+1):
        edges[i] = []
    
    for start, end, cost in road:
        edges[start].append((cost, end))
        edges[end].append((cost, start))
    
    distances = [INF] * (N+1)
    distances[0] = 0
    
    queue = [(0, 1)] #(cost, node)
    
    while queue:
        cost, node = heapq.heappop(queue)
        if cost > distances[node]:
            continue
            
        distances[node] = cost
        
        for new_cost, new_node in edges[node]:
            if distances[new_node] > cost + new_cost:
                heapq.heappush(queue, (new_cost+cost, new_node))
                
    

    return len(list(filter(lambda x: x<= K, distances[1:])))