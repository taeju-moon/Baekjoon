import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bags = [index for index in range(0, N+1, 1)]

for _ in range(M):
    i, j = map(int, input().split())
    bags = bags[:i] + list(reversed(bags[i:j+1])) + \
        (bags[j+1:] if j+1 < N+1 else [])

for bag in bags[1:]:
    print(bag, end=" ")
