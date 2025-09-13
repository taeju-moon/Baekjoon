'''
이진탐색 사용
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

datas = list(map(int, input().split()))

lower_bound = 0  # 길이가 작아서 가능한 톱
upper_bound = max(datas)  # 길이가 커서 불가능한 톱
current_tob = int(upper_bound / 2)

while upper_bound != lower_bound + 1:
    # 베어갈 수 있는 나무의 길이 계산
    tree_length = 0
    for data in datas:
        if data > current_tob:
            tree_length += data-current_tob
    # 베어갈 수 있는 나무의 길이가 딱 맞아 떨어질 경우
    if tree_length == M:
        lower_bound = current_tob
        break
    # 베어갈 수 있는 나무의 길이가 충분할 경우
    if tree_length > M:
        lower_bound = max(current_tob, lower_bound)
        current_tob = int((lower_bound + upper_bound) / 2)
        continue
    # 베어갈 수 있는 나무의 길이가 부족할 경우
    if tree_length < M:
        upper_bound = min(current_tob, upper_bound)
        current_tob = int((lower_bound + upper_bound) / 2)
        continue
print(lower_bound)
