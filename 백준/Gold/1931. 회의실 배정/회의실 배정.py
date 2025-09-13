import sys
input = sys.stdin.readline

N = int(input())
cases = []  # (시작점, 끝점)[]
for _ in range(N):
    a, b = map(int, input().split())
    cases.append((a, b))

cases.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간이 적은 순으로 정렬

count = 0
last_data = (0, 0)
for case in cases:
    if case[0] >= last_data[1]:
        count += 1
        last_data = case
print(count)
