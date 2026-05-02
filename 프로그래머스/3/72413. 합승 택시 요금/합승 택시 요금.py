import sys
INF = sys.maxsize

def solution(n, s, a, b, fares):
    dist = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
    for fare in fares:
        start, end, cost = fare
        dist[start][end] = cost
        dist[end][start] = cost
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
                

    cost2 = INF
    for k in range(1, n+1):
        cost2 = min(cost2, dist[s][k] + dist[k][a] + dist[k][b])
    return cost2