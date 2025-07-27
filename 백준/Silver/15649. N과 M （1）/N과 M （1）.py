'''
1. 아이디어
- 백트래킹 재귀함수 안에서 for문을 돌면서 숫자 선택
- 재귀함수에서 M개 선택할 경우 print
2. 시간복잡도
- N! > 가능
2. 자료구조
- 방문여부 확인 배열: bool[]
- 선택한 값 저장 배열: int[]
'''

import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


N, M = map(int, input().split())

result = []
visited = [False] * (N+1)


def recur(num):
    if num == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N+1, 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            recur(num+1)

            result.pop()
            visited[i] = False


recur(0)
