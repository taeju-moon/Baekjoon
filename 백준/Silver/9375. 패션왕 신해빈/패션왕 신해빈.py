N = int(input())

final_result = []


def process():
    N = int(input())
    hash = {}
    for _ in range(N):
        name, category = input().split()
        if hash.get(category):
            hash[category] += 1
        else:
            hash[category] = 1

    result = 1
    for key in hash:
        value = hash[key]
        result *= (value+1)
    final_result.append(result-1)


for _ in range(N):
    process()

for result in final_result:
    print(result)
