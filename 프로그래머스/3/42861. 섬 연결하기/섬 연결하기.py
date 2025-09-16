import heapq

def solution(n, costs):
    edges = [[] for _ in range(n)]
    visited = [False] * (n)

    for start, end,cost in costs:
        edges[start].append((cost, end))
        edges[end].append((cost, start))
        
    heap = [(0,0)]
    answer = 0
    while heap:
        cost, node = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        answer += cost
        for new_cost, new_node in edges[node]:
            if not visited[new_node]:
                heapq.heappush(heap, (new_cost, new_node))
    return answer