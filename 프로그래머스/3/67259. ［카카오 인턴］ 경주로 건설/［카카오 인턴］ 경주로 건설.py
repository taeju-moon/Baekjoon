import heapq
import sys

INF = sys.maxsize

def solution(board):
    y_len = len(board)
    x_len = len(board[0])
    
    distance = [[[INF] * 2 for _ in range(x_len)] for _ in range(y_len)]
    distance[0][0][0] = 0 #수평 진입 최소값
    distance[0][0][1] = 0 # 수직 진입 최소값
    
    #N은 상관없음, H는 수평, V는 수직
    queue = [(0, 0, 0, "N")] # (cost, y, x, 방향(H 또는 V 또는 N) )
    

    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    while queue:
        cost, y, x, direction = heapq.heappop(queue)
        
        
        for i in range(4):
            next_direction = "H" if dy[i] == 0 else "V"
            
            next_y = y + dy[i]
            next_x = x + dx[i]
            
            if 0 <= next_y < y_len and 0 <= next_x < x_len:
            
                new_cost = 100 if (direction == "N" or direction == next_direction) else 600
                
                direction_num = 0 if next_direction == "H" else 1

                if distance[next_y][next_x][direction_num] >= cost + new_cost and not board[next_y][next_x]:
                    distance[next_y][next_x][direction_num] = cost + new_cost
                    heapq.heappush(queue, (cost+new_cost, next_y, next_x, next_direction))
                
    return min(distance[y_len-1][x_len-1])