import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

datas = permutations(range(1, N+1, 1), M)

for data in datas:
    for d in data:
        print(d, end=" ")
    print()
