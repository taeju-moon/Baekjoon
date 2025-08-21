'''
1759 암호만들기

- 최소 한 개의 모음과 최소 2개의 자음
- 증가하는 순서로 배열

L = 자릿수
C = 문자의 개수


'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


L, C = map(int, input().split())
datas = list(input().split())
datas.sort()


def validate_word(words):
    ja = 0
    mo = 0
    for w in words:
        if w in "aeiou":
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1


words = []


def backtracking(count, index):
    if count == L:
        if validate_word(words):
            print("".join(words))
        return

    for i in range(index, C):
        if datas[i] not in words:
            words.append(datas[i])
            backtracking(count+1, i)
            words.pop()


backtracking(0, 0)
