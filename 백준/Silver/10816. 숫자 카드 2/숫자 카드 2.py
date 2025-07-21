N = int(input())
standard_numbers = map(int, input().split())

M = int(input())
nums_to_find = map(int, input().split())

hash = {}
for num in standard_numbers:
    if hash.get(num):
        hash[num] += 1
    else:
        hash[num] = 1


for num in nums_to_find:
    if hash.get(num):
        print(hash[num], end=" ")
    else:
        print(0, end=" ")