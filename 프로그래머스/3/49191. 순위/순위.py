def solution(n, results):
    dist = [["?"] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = "F"
        
    for a,b in results:
        dist[a-1][b-1] = "+"
        dist[b-1][a-1] = "-"
    

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] != "?":
                    continue
                if dist[i][k] == "-" and dist[k][j] == "-":
                    dist[i][j] = "-"
                    continue
                if dist[i][k] == "+" and dist[k][j] == "+":
                    dist[i][j] = "+"
    

    answer = 0
    for i in range(n):
        ok = True
        for j in range(n):
            if dist[i][j] == "?":
                ok = False
                break
                
        if ok: answer +=1
    return answer