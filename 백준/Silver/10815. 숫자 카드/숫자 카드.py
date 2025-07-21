N = int(input())
standard_nums = map(int, input().split())

M = int(input())
nums_to_find = map(int, input().split())

hash = {}
for num in standard_nums:
    hash[num] = 1

for num in nums_to_find:
    if hash.get(num):
        print(1, end=" ")
    else:
        print(0, end=" ")
