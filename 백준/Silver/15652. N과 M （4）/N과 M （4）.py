'''
중복 조합
'''

from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

datas = combinations_with_replacement(range(1, N+1, 1), M)

for data in datas:
    for d in data:
        print(d, end=" ")
    print()
