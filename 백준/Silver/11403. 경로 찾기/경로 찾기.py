import sys

input = sys.stdin.readline

N = int(input())

matrix = []
distances = [ [False] * (N) for _ in range(N)]

for _ in range(N):
    matrix.append(list(map(int, input().split())))


for i in range(N):
    for j in range(N):
        for k in range(N):
            if matrix[i][j]:
                distances[i][j] = True
            if matrix[i][k] and matrix[k][j]:
                distances[i][j] = True
                matrix[i][j] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if matrix[i][j]:
                distances[i][j] = True
            if matrix[i][k] and matrix[k][j]:
                distances[i][j] = True
                matrix[i][j] = 1

for i in range(N):
    for j in range(N):
        print(1 if distances[i][j] else 0, end=" ")
    print()