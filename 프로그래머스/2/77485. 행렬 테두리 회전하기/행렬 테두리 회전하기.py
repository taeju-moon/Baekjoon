def solution(rows, columns, queries):
    answer = []
    
    # 행렬 채우기
    matrix = [[0] * (columns+1) for _ in range(rows+1)]
    
    
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i+1][j+1] = cnt
            cnt +=1
    
    
    # 쿼리 실행
    temp = [[0] * (columns+1) for _ in range(rows+1)] # 변경된 직사각형을 만들기 위한 예비분
    for query in queries:
        x1, y1, x2, y2 = query
        
        # 윗 면 칠하기
        for i in range(y1, y2+1):
            # 처음의 경우는 왼쪽 면에서 가져오기
            if i == y1:
                temp[x1][i] = matrix[x1+1][i]
            else:
                temp[x1][i] = matrix[x1][i-1]

        # 오른쪽 면 칠하기
        for i in range(x1+1, x2):
            temp[i][y2] = matrix[i-1][y2]
            
        # 왼쪽 면 칠하기
        for i in range(x2-1, x1, -1):
            temp[i][y1] = matrix[i+1][y1]
            
        # 아랫면 칠하기
        for i in range(y2, y1-1, -1):
            if i == y2:
                temp[x2][i] = matrix[x2-1][i]
            else:
                temp[x2][i] = matrix[x2][i+1]
                
        min_val = 1000000
        # temp를 matrix로 옮기면서 answer을 끼워넣기
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if i == x1 or i == x2 or j == y1 or j == y2: # 테두리만 복사
                    min_val = min(min_val, temp[i][j])
                    matrix[i][j] = temp[i][j]
        answer.append(min_val)
    return answer