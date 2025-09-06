'''
1. 아이디어
- 처음 k개의 값을 구함
- for문: 다음 인덱스의 값을 더하고, 앞의 값을 뺌
- 이때 최대 값을 갱신
2. 시간복잡도
- O(n)
3. 자료구조
- 전체 정수 배열: int[]
- 합한 수 int
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
datas = list(map(int, input().split()))

max_val = 0  # K의 값의 합을 저장하는 변수

each = 0
# K개를 더해주기
for i in range(K):
    each += datas[i]
max_val = each

# 다음 인덱스 더해주고, 이전 인덱스 빼주기
for i in range(K, N):
    each += datas[i]
    each -= datas[i-K]

    max_val = max(max_val, each)

print(max_val)
