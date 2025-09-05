import sys
input = sys.stdin.readline

N, M = map(int, input().split())
datas = list(map(int, input().split()))
datas.sort()
visited = [False] * N
stack = []


def backtrack(num):
    if len(stack) == M:
        print(" ".join(map(str, stack)))
    for i in range(num, N):
        if not visited[i]:
            visited[i] = True
            stack.append(datas[i])
            backtrack(i)
            stack.pop()
            visited[i] = False


backtrack(0)
