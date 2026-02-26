import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(100000)

A, B, C = map(int, input().split())

hash = {}
queue = deque()
queue.append((0,0,C))

results = set()

def add_new_node(node):
    if node not in hash:
        hash[node] = True
        queue.append(node)

capacity = [A,B,C]
def get_new_node(a,b,c, from_, to_):
    nodes = [a,b,c]
    if nodes[from_] + nodes[to_] <= capacity[to_]:
        nodes[to_] = nodes[from_] + nodes[to_]
        nodes[from_] = 0
    else:
        nodes[from_] = nodes[from_] - capacity[to_] + nodes[to_]
        nodes[to_] = capacity[to_]
    
    return tuple(nodes)

while queue:
    a,b,c = queue.popleft()
    # 물통에 비어있을때 담기
    if a == 0:
        results.add(c)

    if a != 0:
        node1 = get_new_node(a,b,c,0,1)
        add_new_node(node1)
        node2 = get_new_node(a,b,c,0,2)
        add_new_node(node2)
    if b != 0:
        node1 = get_new_node(a,b,c,1,0)
        add_new_node(node1)
        node2 = get_new_node(a,b,c,1,2)
        add_new_node(node2)
    if c != 0:
        node1 = get_new_node(a,b,c,2,0)
        add_new_node(node1)
        node2 = get_new_node(a,b,c,2,1)
        add_new_node(node2)


for d in sorted(list(results)):
    print(d, end=" ")
    
    