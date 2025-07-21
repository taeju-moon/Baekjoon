N = int(input())
standard_data = map(int, input().split())


M = int(input())
data_to_check = map(int, input().split())

hash = {}
for data in standard_data:
    hash[data] = data

for data in data_to_check:
    if hash.get(data):
        print(1)
    else:
        print(0)
