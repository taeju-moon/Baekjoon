'''
1. 아이디어
- dfs로 모든 경우의 수를 순회하면서
- 최소값 최대값을 구한다
2. 자료구조

'''

N = int(input())

numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

operator_factory = {
    0: lambda a, b: a+b,
    1: lambda a, b: a-b,
    2: lambda a, b: a*b,
    3: lambda a, b: int(a/b)
}

results = []


def dfs(num_idx, result):
    if num_idx == N:
        results.append(result)
        return
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            dfs(num_idx+1, operator_factory[i](result, numbers[num_idx]))
            operators[i] += 1


dfs(1, numbers[0])
print(max(results))
print(min(results))
