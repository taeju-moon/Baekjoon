'''


'''

import sys
input = sys.stdin.readline


N = int(input())

matrix = [[s for s in input()] for _ in range(N)]

max_friends = 0
for current_index, person in enumerate(matrix):
    # 1. 첫번째 줄을 순회하면서 친구들을 찾는다.
    friends_with = [False] * (N)
    for i in range(N):
        if i == current_index:
            continue
        if person[i] == "Y":
            friends_with[i] = True
    secondary_friends = [False] * (N)
    # 2. 해당 친구들에 대해서 2-친구들을 찾는다.
    for i, is_friend in enumerate(friends_with):
        if is_friend:
            for j in range(N):
                if i == j or j == current_index:
                    continue
                if matrix[i][j] == "Y":
                    secondary_friends[j] = True
    # 3. 모든 친구들을 합친다
    for i in range(N):
        if i == current_index:  # 자기 자신은 제외
            continue
        if secondary_friends[i]:
            friends_with[i] = True
    # 4. 최대 친구 수를 계산한다.

    max_friends = max(max_friends, sum(1 if a else 0 for a in friends_with))

print(max_friends)
