import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

matrix = [[str(i) for i in input().split()] for _ in range(N)]


result = 0


def recur(y, x, path):
    global result
    path += matrix[y][x]

    if y == N-1 and x == N-1:
        data = int(path, 2)
        result = max(result, data)
        return

    # case1. 오른쪽으로 한칸 이동
    if x < N-1:
        recur(y, x+1, path)
    # case2. 아래쪽으로 한칸 이동
    if y < N-1:
        recur(y+1, x, path)


recur(0, 0, "")

print(result)
