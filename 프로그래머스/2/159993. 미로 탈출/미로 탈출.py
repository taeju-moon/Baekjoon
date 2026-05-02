import heapq

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    s_point = (0, 0) # (y, x)
    l_point = (0, 0) # (y, x)
    e_point = (0, 0) # (y, x)
    matrix = []
    for i in range(rows):
        arr = []
        word = maps[i]
        for j in range(cols):
            if word[j] == "S":
                s_point = (i, j)
            elif word[j] == "L":
                l_point = (i, j)
            elif word[j] == "E":
                e_point = (i,j)
            arr.append(word[j])
        matrix.append(arr)
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    visited = [[False] * cols for _ in range(rows)]
    
    # 1. 레버를 찾기
    queue = [(0, s_point[0], s_point[1])] #(cost, y, x)
    found = False
    cost_to_l = 0
    while queue:
        cost, y, x = heapq.heappop(queue)
        visited[y][x] = True
        if y == l_point[0] and x == l_point[1]:
            found = True
            cost_to_l = cost
            break
        
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < rows and 0<= nx < cols and matrix[ny][nx] != "X" and not visited[ny][nx]:
                visited[ny][nx] = True
                heapq.heappush(queue, (cost+1, ny, nx))

    if not found:
        return -1
    
    # 2. 출구를 찾기
    found = False
    queue = [(0, l_point[0], l_point[1])] #(cost, y, x)
    cost_to_e = 0
    visited = [[False] * cols for _ in range(rows)]
    while queue:
        cost, y, x = heapq.heappop(queue)
        visited[y][x] = True
        if y == e_point[0] and x == e_point[1]:
            found = True
            cost_to_e = cost
            break
        
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < rows and 0<= nx < cols and matrix[ny][nx] != "X" and not visited[ny][nx]:
                visited[ny][nx] = True
                heapq.heappush(queue, (cost+1, ny, nx))

    if not found:
        return -1
    
    return cost_to_e + cost_to_l