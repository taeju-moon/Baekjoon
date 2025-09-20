import sys
input = sys.stdin.readline

N = int(input())

results = []


def test_case():
    candidates = [0]
    M = int(input())
    count = 0
    while candidates:
        temp = []
        for candidate in candidates:
            if candidate == M:
                count += 1
            elif candidate > M:
                pass
            else:
                temp.append(candidate+1)
                temp.append(candidate+2)
                temp.append(candidate+3)
        candidates = temp
    results.append(count)


for _ in range(N):
    test_case()

for result in results:
    print(result)
