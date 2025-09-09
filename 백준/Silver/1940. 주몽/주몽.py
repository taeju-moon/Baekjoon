

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
materials = list(map(int, input().split()))

arr = [0] * 1000001
for material in materials:
    arr[material] += 1

count = 0
for material in materials:
    if material > M:
        continue
    if material * 2 == M:
        if arr[material] >= 2:
            count += 1
            arr[material] -= 2
        continue
    elif arr[material] > 0 and arr[M-material] > 0:
        count += 1
        arr[material] -= 1
        arr[M-material] -= 1

print(count)
