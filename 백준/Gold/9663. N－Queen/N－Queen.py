'''
1. 아이디어
- 0행부터 Queen놓고 다음 행으로 이동
- visited_default: 어떤 열이 점유되어있는지를 Visited배열로 확인
- visited_plus: 대각선은 i+j값으로 visited2배열로 확인한다
- visited_minus: 대각선 반대는 i-j값으로 체크한다.
2. 자료구조
- visited_default: int[N]
- visited_plus: int[2N]
- visited_minus: int[2N] 
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
visited_default = [0] * N
visited_plus = [0] * 2 * N
visited_minus = [0] * 2 * N
cnt = 0


def dfs(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for j in range(N):
        if visited_default[j] == visited_plus[row+j] == visited_minus[row-j] == 0:
            visited_default[j] = visited_plus[row+j] = visited_minus[row-j] = 1
            dfs(row+1)
            visited_default[j] = visited_plus[row+j] = visited_minus[row-j] = 0


dfs(0)
print(cnt)
