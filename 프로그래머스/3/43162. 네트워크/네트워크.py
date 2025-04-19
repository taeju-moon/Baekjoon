def dfs(visited, node, computers, n):
    found = False
    for i in range(n):
        if not visited[i] and computers[node][i]:
            visited[i] = True
            found = True
            dfs(visited,i,computers,n)

    return found

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for root in range(n):
        found = dfs(visited, root, computers, n)
        if found: answer += 1
        if all(visited): break
    return answer