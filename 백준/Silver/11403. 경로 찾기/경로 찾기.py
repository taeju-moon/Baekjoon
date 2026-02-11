import sys

input = sys.stdin.readline

N = int(input())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))


for k in range(N):
    for i in range(N):
        for j in range(N):
            if matrix[i][k] and matrix[k][j]:
                matrix[i][j] = True

for i in range(N):
    for j in range(N):
        print(1 if matrix[i][j] else 0, end=" ")
    print()