N, M = map(int, input().split())

hash = {}

for i in range(N):
    data = input()
    hash[data] = True

results = []

for i in range(M):
    data = input()
    if hash.get(data):
        results.append(data)

results.sort()
print(len(results))
for result in results:
    print(result)
