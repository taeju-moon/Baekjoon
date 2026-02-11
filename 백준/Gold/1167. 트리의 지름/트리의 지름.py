import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

adj_list = [[] for _ in range(N+1)] #(node, cost)

for _ in range(N):
    datas = list(map(int, input().split()))
    index = 1
    node = datas[0]
    while index < len(datas)-1:
        adj_list[node].append((datas[index], datas[index+1]))
        index += 2

# return (node, cost)
def get_far_node(start):
    queue = deque()
    queue.append((start, 0))
    visited = [False] * (N+1)
    result_node = start
    result_cost = 0

    while queue:
        node, cost = queue.popleft()
        visited[node] = True
        if cost > result_cost:
            result_cost = cost
            result_node = node
        for next_node, next_cost in adj_list[node]:
            if not visited[next_node]:
                queue.append((next_node, cost + next_cost))

    return (result_node, result_cost)



# 1. 첫번째 순회로 임의의 노드에서 가장 먼 노드 찾기
node1, cost1 = get_far_node(1)

# 2. 1에서 나온 결과에서 가장 먼 노드 찾기
node2, cost2 = get_far_node(node1)

print(cost2)