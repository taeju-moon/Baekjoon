N, M = map(int, input().split())

hash = {}

for i in range(N):
    data = input()
    hash[data] = 1

count = 0
for j in range(M):
    data = input()
    if hash.get(data):
        count += 1

print(count)
