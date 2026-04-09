from collections import deque

def solution(maps):
    y_len = len(maps)
    x_len = len(maps[0])
    y = 0
    x = 0
    visited = [[False] * x_len for _ in range(y_len)]
    
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    queue = deque() #(cost, y, x)
    queue.append((1, y, x))
    visited[y][x] = True
    
    while queue:
        cost, y, x = queue.popleft()
        if y == y_len - 1 and x == x_len -1:
            return cost
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if 0<= new_y < y_len and 0 <= new_x < x_len and not visited[new_y][new_x] and maps[new_y][new_x]:
                visited[new_y][new_x] = True
                queue.append((cost+1, new_y, new_x))
    return -1