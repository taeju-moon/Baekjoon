import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

datas = combinations(range(1, N+1, 1), M)

for data in datas:
    for d in data:
        print(d, end=" ")
    print()
