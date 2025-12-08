import sys

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())

E = int(input())

matrix = [[INF if j != i else 0 for j in range(N)] for i in range(N)]

for _ in range(E):
    a, b, cost = map(int, input().split())
    a -= 1
    b -= 1
    if matrix[a][b] > cost:
        matrix[a][b] = cost

for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]


for i in range(N):
    for j in range(N):
        data = matrix[i][j]
        print(data if data != INF else 0, end=" ")
    print()
