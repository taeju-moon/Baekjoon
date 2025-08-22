import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = [0] * (N+1)


for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i, j+1, 1):
        result[index] = k

for data in result[1:]:
    print(data, end=" ")
