import sys
input = sys.stdin.readline

N = int(input())

start = 1
end = 2
using_sum = 1
count = 0
if using_sum == N:
    count += 1
while end <= N and start <= end:
    temp_sum = using_sum + end
    if temp_sum == N:
        count += 1
        end += 1
        using_sum = temp_sum
    elif temp_sum < N:
        end += 1
        using_sum = temp_sum
    elif temp_sum > N:
        using_sum -= start
        start += 1
        if start > end:
            end = start

print(count)
