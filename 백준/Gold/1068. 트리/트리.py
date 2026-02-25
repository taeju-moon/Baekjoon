import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

datas = list(map(int, input().split()))
adj_list = [[] for _ in range(N) ]

for i in range(N):
    if datas[i] == -1:
        continue
    adj_list[datas[i]].append(i)

root = datas.index(-1)


count = 0
visited = [False] * N
def dfs(node):
    global count
    if len(adj_list[node]) == 0:
        count+=1
    else:
        for next_node in adj_list[node]:
            if not visited[next_node]:
                dfs(next_node)

M = int(input())
if M != root:
    adj_list[M] = []
    m_parent = datas[M]
    adj_list[m_parent].remove(M)
    dfs(root)

print(count)