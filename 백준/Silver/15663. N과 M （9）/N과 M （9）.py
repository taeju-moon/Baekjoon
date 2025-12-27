import sys
input = sys.stdin.readline

N, M = map(int, input().split())

datas = list(map(int, input().split()))
N = len(datas)
datas.sort()

arr = []

indexes = []

results = {}


def backtracking(num, index):
    if num == M:
        result = " ".join(map(str, arr))
        if result not in results:
            results[result] = True
            print(result)
        return

    for i in range(0, N):
        if i in indexes:
            continue
        indexes.append(i)
        arr.append(datas[i])
        backtracking(num+1, i)
        arr.pop()
        indexes.pop()


backtracking(0, 0)
