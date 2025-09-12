'''
1. 아이디어
- dp 사용
- dps 라는 리스트를 구현
2. 자료구조
'''

import sys
input = sys.stdin.readline

N = int(input())
datas = [0] * N
dps = []  # [스택이 한 칸 쌓였을때의 최댓값, 스택이 두 칸 쌓였을때의 최댓값]
for i in range(N):
    datas[i] = int(input())
    dps.append({1: 0, 2: 0})

result = 0

for i in range(N):
    if i == 0:  # 첫번째 요소는 그대로 넣기
        dps[0][1] = datas[0]
        continue
    if i == 1:  # 두번째 요소는 따로 처리
        dps[1][2] = dps[0][1] + datas[1]
        dps[1][1] = datas[1]
        continue
    # 바로 이전 곳에서 왔을 경우
    dps[i][2] = dps[i-1][1] + datas[i]  # 바로 이전 곳의 1스택만 사용할 수 있음
    # 두칸 이전 곳에서 왔을 경우
    dps[i][1] = max(dps[i-2][1], dps[i-2][2]) + \
        datas[i]  # 두 칸 이전 곳의 1스택 또는 2스택을 사용 가ㅡㄴㅇ

print(max(dps[-1][1], dps[-1][2]))
